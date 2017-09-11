#ifndef PHOSPHOR_MASK_RESIZING_H
#define PHOSPHOR_MASK_RESIZING_H

/////////////////////////////  GPL LICENSE NOTICE  /////////////////////////////

//  crt-royale: A full-featured CRT shader, with cheese.
//  Copyright (C) 2014 TroggleMonkey <trogglemonkey@gmx.com>
//
//  This program is free software; you can redistribute it and/or modify it
//  under the terms of the GNU General Public License as published by the Free
//  Software Foundation; either version 2 of the License, or any later version.
//
//  This program is distributed in the hope that it will be useful, but WITHOUT
//  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
//  FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
//  more details.
//
//  You should have received a copy of the GNU General Public License along with
//  this program; if not, write to the Free Software Foundation, Inc., 59 Temple
//  Place, Suite 330, Boston, MA 02111-1307 USA


//////////////////////////////////  INCLUDES  //////////////////////////////////

#include "../user-settings.h"
#include "derived-settings-and-constants.h"

/////////////////////////////  CODEPATH SELECTION  /////////////////////////////

//  Choose a looping strategy based on what's allowed:
//  Dynamic loops not allowed: Use a flat static loop.
//  Dynamic loops accomodated: Coarsely branch around static loops.
//  Dynamic loops assumed allowed: Use a flat dynamic loop.
#ifndef DRIVERS_ALLOW_DYNAMIC_BRANCHES
    #ifdef ACCOMODATE_POSSIBLE_DYNAMIC_LOOPS
        #define BREAK_LOOPS_INTO_PIECES
    #else
        #define USE_SINGLE_STATIC_LOOP
    #endif
#endif  //  No else needed: Dynamic loops assumed.


    #define CALCULATE_R_COORD_FOR_4_SAMPLES                                    \
        const vec4 true_i = vec4(i_base + i) + vec4(0.0, 1.0, 2.0, 3.0); \
        const vec4 tile_uv_r = fract(                                         \
            first_texel_tile_uv_rrrr + true_i * tile_dr);                      \
        const vec4 tex_uv_r = tile_uv_r * tile_size_uv_r;

    #define VERTICAL_SINC_RESAMPLE_LOOP_BODY                                   \
        CALCULATE_R_COORD_FOR_4_SAMPLES;                                       \
        const vec3 new_sample0 = tex2Dlod0try(texture,                       \
            vec2(tex_uv.x, tex_uv_r.x)).rgb;                                 \
        const vec3 new_sample1 = tex2Dlod0try(texture,                       \
            vec2(tex_uv.x, tex_uv_r.y)).rgb;                                 \
        const vec3 new_sample2 = tex2Dlod0try(texture,                       \
            vec2(tex_uv.x, tex_uv_r.z)).rgb;                                 \
        const vec3 new_sample3 = tex2Dlod0try(texture,                       \
            vec2(tex_uv.x, tex_uv_r.w)).rgb;                                 \
        UPDATE_COLOR_AND_WEIGHT_SUMS;
		
	#define UPDATE_COLOR_AND_WEIGHT_SUMS                                       \
        const vec4 dist = magnification_scale *                              \
            abs(first_dist_unscaled - true_i);                                 \
        const vec4 pi_dist = pi * dist;                                      \
        CALCULATE_SINC_RESAMPLE_WEIGHTS;                                       \
        pixel_color += new_sample0 * weights.xxx;                              \
        pixel_color += new_sample1 * weights.yyy;                              \
        pixel_color += new_sample2 * weights.zzz;                              \
        pixel_color += new_sample3 * weights.www;                              \
        weight_sum += weights;
		
	#ifdef PHOSPHOR_MASK_RESIZE_LANCZOS_WINDOW
        #define CALCULATE_SINC_RESAMPLE_WEIGHTS                                \
            const vec4 pi_dist_over_lobes = pi_over_lobes * dist;            \
            const vec4 weights = min(sin(pi_dist) * sin(pi_dist_over_lobes) /\
                (pi_dist*pi_dist_over_lobes), vec4(1.0));
    #else
        #define CALCULATE_SINC_RESAMPLE_WEIGHTS                                \
            const vec4 weights = min(sin(pi_dist)/pi_dist, vec4(1.0));
    #endif
	
	#define HORIZONTAL_SINC_RESAMPLE_LOOP_BODY                                 \
        CALCULATE_R_COORD_FOR_4_SAMPLES;                                       \
        const vec3 new_sample0 = tex2Dlod0try(texture,                       \
            vec2(tex_uv_r.x, tex_uv.y)).rgb;                                 \
        const vec3 new_sample1 = tex2Dlod0try(texture,                       \
            vec2(tex_uv_r.y, tex_uv.y)).rgb;                                 \
        const vec3 new_sample2 = tex2Dlod0try(texture,                       \
            vec2(tex_uv_r.z, tex_uv.y)).rgb;                                 \
        const vec3 new_sample3 = tex2Dlod0try(texture,                       \
            vec2(tex_uv_r.w, tex_uv.y)).rgb;                                 \
        UPDATE_COLOR_AND_WEIGHT_SUMS;

//////////////////////////////////  CONSTANTS  /////////////////////////////////

//  The larger the resized tile, the fewer samples we'll need for downsizing.
//  See if we can get a static min tile size > mask_min_allowed_tile_size:
const float mask_min_allowed_tile_size = ceil(
    mask_min_allowed_triad_size * mask_triads_per_tile);
const float mask_min_expected_tile_size = 
        mask_min_allowed_tile_size;
//  Limit the number of sinc resize taps by the maximum minification factor:
const float pi_over_lobes = pi/mask_sinc_lobes;
const float max_sinc_resize_samples_float = 2.0 * mask_sinc_lobes *
    mask_resize_src_lut_size.x/mask_min_expected_tile_size;
//  Vectorized loops sample in multiples of 4.  Round up to be safe:
const float max_sinc_resize_samples_m4 = ceil(
    max_sinc_resize_samples_float * 0.25) * 4.0;
	
	/////////////////////////  RESAMPLING FUNCTION HELPERS  ////////////////////////

float get_dynamic_loop_size(const float magnification_scale)
{
    //  Requires:   The following global constants must be defined:
    //              1.) mask_sinc_lobes
    //              2.) max_sinc_resize_samples_m4
    //  Returns:    The minimum number of texture samples for a correct downsize
    //              at magnification_scale.
    //  We're downsizing, so the filter is sized across 2*lobes output pixels
    //  (not 2*lobes input texels).  This impacts distance measurements and the
    //  minimum number of input samples needed.
    const float min_samples_float = 2.0 * mask_sinc_lobes / magnification_scale;
    const float min_samples_m4 = ceil(min_samples_float * 0.25) * 4.0;
    #ifdef DRIVERS_ALLOW_DYNAMIC_BRANCHES
        const float max_samples_m4 = max_sinc_resize_samples_m4;
    #else   // ifdef BREAK_LOOPS_INTO_PIECES
        //  Simulating loops with branches imposes a 128-sample limit.
        const float max_samples_m4 = min(128.0, max_sinc_resize_samples_m4);
    #endif
    return min(min_samples_m4, max_samples_m4);
}

vec2 get_first_texel_tile_uv_and_dist(const vec2 tex_uv, 
    const vec2 texture_size, const float dr, 
    const float input_tiles_per_texture_r, const float samples,
    const bool vertical)
{
    //  Requires:   1.) dr == du == 1.0/texture_size.x or
    //                  dr == dv == 1.0/texture_size.y
    //                  (whichever direction we're resampling in).
    //                  It's a scalar to save register space.
    //              2.) input_tiles_per_texture_r is the number of input tiles
    //                  that can fit in the input texture in the direction we're
    //                  resampling this pass.
    //              3.) vertical indicates whether we're resampling vertically
    //                  this pass (or horizontally).
    //  Returns:    Pack and return the first sample's tile_uv coord in [0, 1]
    //              and its texel distance from the destination pixel, in the
    //              resized dimension only.
    //  We'll start with the topmost or leftmost sample and work down or right,
    //  so get the first sample location and distance.  Modify both dimensions
    //  as if we're doing a one-pass 2D resize; we'll throw away the unneeded
    //  (and incorrect) dimension at the end.
    const vec2 curr_texel = tex_uv * texture_size;
    const vec2 prev_texel =
        floor(curr_texel - vec2(under_half)) + vec2(0.5);
    const vec2 first_texel = prev_texel - vec2(samples/2.0 - 1.0);
    const vec2 first_texel_uv_wrap_2D = first_texel * dr;
    const vec2 first_texel_dist_2D = curr_texel - first_texel;
    //  Convert from tex_uv to tile_uv coords so we can sub fracts for fmods.
    const vec2 first_texel_tile_uv_wrap_2D =
        first_texel_uv_wrap_2D * input_tiles_per_texture_r;
    //  Project wrapped coordinates to the [0, 1] range.  We'll do this with all
    //  samples,but the first texel is special, since it might be negative.
    vec2 coord_negative = vec2(0.0);
        if(first_texel_tile_uv_wrap_2D.x < 0.0) coord_negative.x = first_texel_tile_uv_wrap_2D.x;
		if(first_texel_tile_uv_wrap_2D.x < 0.0) coord_negative.y = first_texel_tile_uv_wrap_2D.y;
    const vec2 first_texel_tile_uv_2D =
        fract(first_texel_tile_uv_wrap_2D) + coord_negative;
    //  Pack the first texel's tile_uv coord and texel distance in 1D:
    const vec2 tile_u_and_dist =
        vec2(first_texel_tile_uv_2D.x, first_texel_dist_2D.x);
    const vec2 tile_v_and_dist =
        vec2(first_texel_tile_uv_2D.y, first_texel_dist_2D.y);
    return vertical ? tile_v_and_dist : tile_u_and_dist;
    //return mix(tile_u_and_dist, tile_v_and_dist, float(vertical));
}

vec4 tex2Dlod0try(const sampler2D tex, const vec2 tex_uv)
{
    //  Mipmapping and anisotropic filtering get confused by sinc-resampling.
    //  One [slow] workaround is to select the lowest mip level:
    #ifdef ANISOTROPIC_RESAMPLING_COMPAT_TEX2DLOD
        return tex2Dlod(tex, vec4(tex_uv, 0.0, 0.0));
    #else
        #ifdef ANISOTROPIC_RESAMPLING_COMPAT_TEX2DBIAS
            return tex2Dbias(tex, vec4(tex_uv, 0.0, -16.0));
        #else
            return texture(tex, tex_uv);
        #endif
    #endif
}
	
////////////////////////////  TILE SIZE CALCULATION  ///////////////////////////

vec2 get_resized_mask_tile_size(const vec2 estimated_viewport_size,
    const vec2 estimated_mask_resize_output_size,
    const bool solemnly_swear_same_inputs_for_every_pass)
{
    //  Requires:   The following global constants must be defined according to
    //              certain constraints:
    //              1.) mask_resize_num_triads: Must be high enough that our
    //                  mask sampling method won't have artifacts later
    //                  (long story; see derived-settings-and-constants.h)
    //              2.) mask_resize_src_lut_size: Texel size of our mask LUT
    //              3.) mask_triads_per_tile: Num horizontal triads in our LUT
    //              4.) mask_min_allowed_triad_size: User setting (the more
    //                  restrictive it is, the faster the resize will go)
    //              5.) mask_min_allowed_tile_size_x < mask_resize_src_lut_size.x
    //              6.) mask_triad_size_desired_{runtime, static}
    //              7.) mask_num_triads_desired_{runtime, static}
    //              8.) mask_specify_num_triads must be 0.0/1.0 (false/true)
    //              The function parameters must be defined as follows:
    //              1.) estimated_viewport_size == (final viewport size);
    //                  If mask_specify_num_triads is 1.0/true and the viewport
    //                  estimate is wrong, the number of triads will differ from
    //                  the user's preference by about the same factor.
    //              2.) estimated_mask_resize_output_size: Must equal the
    //                  output size of the MASK_RESIZE pass.
    //                  Exception: The x component may be estimated garbage if
    //                  and only if the caller throws away the x result.
    //              3.) solemnly_swear_same_inputs_for_every_pass: Set to false,
    //                  unless you can guarantee that every call across every
    //                  pass will use the same sizes for the other parameters.
    //              When calling this across multiple passes, always use the
    //              same y viewport size/scale, and always use the same x
    //              viewport size/scale when using the x result.
    //  Returns:    Return the final size of a manually resized mask tile, after
    //              constraining the desired size to avoid artifacts.  Under
    //              unusual circumstances, tiles may become stretched vertically
    //              (see wall of text below).
    //  Stated tile properties must be correct:
    const float tile_aspect_ratio_inv =
        mask_resize_src_lut_size.y/mask_resize_src_lut_size.x;
    const float tile_aspect_ratio = 1.0/tile_aspect_ratio_inv;
    const vec2 tile_aspect = vec2(1.0, tile_aspect_ratio_inv);
    //  If mask_specify_num_triads is 1.0/true and estimated_viewport_size.x is
    //  wrong, the user preference will be misinterpreted:
    const float desired_tile_size_x = mask_triads_per_tile * mix(
        params.mask_triad_size_desired,
        estimated_viewport_size.x / params.mask_num_triads_desired,
        params.mask_specify_num_triads);
    if(params.mask_sample_mode_desired > 0.5)
    {
        //  We don't need constraints unless we're sampling MASK_RESIZE.
        return desired_tile_size_x * tile_aspect;
    }
    //  Make sure we're not upsizing:
    const float temp_tile_size_x =
        min(desired_tile_size_x, mask_resize_src_lut_size.x);
    //  Enforce min_tile_size and max_tile_size in both dimensions:
    const vec2 temp_tile_size = temp_tile_size_x * tile_aspect;
    const vec2 min_tile_size =
        mask_min_allowed_tile_size * tile_aspect;
    const vec2 max_tile_size =
        estimated_mask_resize_output_size / mask_resize_num_tiles;
    const vec2 clamped_tile_size =
        clamp(temp_tile_size, min_tile_size, max_tile_size);
    //  Try to maintain tile_aspect_ratio.  This is the tricky part:
    //  If we're currently resizing in the y dimension, the x components
    //  could be MEANINGLESS.  (If estimated_mask_resize_output_size.x is
    //  bogus, then so is max_tile_size.x and clamped_tile_size.x.)
    //  We can't adjust the y size based on clamped_tile_size.x.  If it
    //  clamps when it shouldn't, it won't clamp again when later passes
    //  call this function with the correct sizes, and the discrepancy will
    //  break the sampling coords in MASKED_SCANLINES.  Instead, we'll limit
    //  the x size based on the y size, but not vice versa, unless the
    //  caller swears the parameters were the same (correct) in every pass.
    //  As a result, triads could appear vertically stretched if:
    //  a.) mask_resize_src_lut_size.x > mask_resize_src_lut_size.y: Wide
    //      LUT's might clamp x more than y (all provided LUT's are square)
    //  b.) true_viewport_size.x < true_viewport_size.y: The user is playing
    //      with a vertically oriented screen (not accounted for anyway)
    //  c.) mask_resize_viewport_scale.x < masked_resize_viewport_scale.y:
    //      Viewport scales are equal by default.
    //  If any of these are the case, you can fix the stretching by setting:
    //      mask_resize_viewport_scale.x = mask_resize_viewport_scale.y *
    //          (1.0 / min_expected_aspect_ratio) *
    //          (mask_resize_src_lut_size.x / mask_resize_src_lut_size.y)
    const float x_tile_size_from_y =
        clamped_tile_size.y * tile_aspect_ratio;
    const float y_tile_size_from_x = mix(clamped_tile_size.y,
        clamped_tile_size.x * tile_aspect_ratio_inv,
        float(solemnly_swear_same_inputs_for_every_pass));
    const vec2 reclamped_tile_size = vec2(
        min(clamped_tile_size.x, x_tile_size_from_y),
        min(clamped_tile_size.y, y_tile_size_from_x));
    //  We need integer tile sizes in both directions for tiled sampling to
    //  work correctly.  Use floor (to make sure we don't round up), but be
    //  careful to avoid a rounding bug where floor decreases whole numbers:
    const vec2 final_resized_tile_size =
        floor(reclamped_tile_size + vec2(FIX_ZERO(0.0)));
    return final_resized_tile_size;
}

/////////////////////////  FINAL MASK SAMPLING HELPERS  ////////////////////////

vec4 get_mask_sampling_parameters(const vec2 mask_resize_texture_size,
    const vec2 mask_resize_video_size, const vec2 true_viewport_size,
    out vec2 mask_tiles_per_screen)
{
    //  Requires:   1.) Requirements of get_resized_mask_tile_size() must be
    //                  met, particularly regarding global constants.
    //              The function parameters must be defined as follows:
    //              1.) mask_resize_texture_size == MASK_RESIZE.texture_size
    //                  if get_mask_sample_mode() is 0 (otherwise anything)
    //              2.) mask_resize_video_size == MASK_RESIZE.video_size
    //                  if get_mask_sample_mode() is 0 (otherwise anything)
    //              3.) true_viewport_size == IN.output_size for a pass set to
    //                  1.0 viewport scale (i.e. it must be correct)
    //  Returns:    Return a vec4 containing:
    //                  xy: tex_uv coords for the start of the mask tile
    //                  zw: tex_uv size of the mask tile from start to end
    //              mask_tiles_per_screen is an out parameter containing the
    //              number of mask tiles that will fit on the screen.
    //  First get the final resized tile size.  The viewport size and mask
    //  resize viewport scale must be correct, but don't solemnly swear they
    //  were correct in both mask resize passes unless you know it's true.
    //  (We can better ensure a correct tile aspect ratio if the parameters are
    //  guaranteed correct in all passes...but if we lie, we'll get inconsistent
    //  sizes across passes, resulting in broken texture coordinates.)
    const float mask_sample_mode = params.mask_sample_mode_desired;//get_mask_sample_mode();
    const vec2 mask_resize_tile_size = get_resized_mask_tile_size(
        true_viewport_size, mask_resize_video_size, false);
    if(mask_sample_mode < 0.5)
    {
        //  Sample MASK_RESIZE: The resized tile is a fracttion of the texture
        //  size and starts at a nonzero offset to allow for border texels:
        const vec2 mask_tile_uv_size = mask_resize_tile_size /
            mask_resize_texture_size;
        const vec2 skipped_tiles = mask_start_texels/mask_resize_tile_size;
        const vec2 mask_tile_start_uv = skipped_tiles * mask_tile_uv_size;
        //  mask_tiles_per_screen must be based on the *true* viewport size:
        mask_tiles_per_screen = true_viewport_size / mask_resize_tile_size;
        return vec4(mask_tile_start_uv, mask_tile_uv_size);
    }
    else
    {
        //  If we're tiling at the original size (1:1 pixel:texel), redefine a
        //  "tile" to be the full texture containing many triads.  Otherwise,
        //  we're hardware-resampling an LUT, and the texture truly contains a
        //  single unresized phosphor mask tile anyway.
        const vec2 mask_tile_uv_size = vec2(1.0);
        const vec2 mask_tile_start_uv = vec2(0.0);
        if(mask_sample_mode > 1.5)
        {
            //  Repeat the full LUT at a 1:1 pixel:texel ratio without resizing:
            mask_tiles_per_screen = true_viewport_size/mask_texture_large_size;
        }
        else
        {
            //  Hardware-resize the original LUT:
            mask_tiles_per_screen = true_viewport_size / mask_resize_tile_size;
        }
        return vec4(mask_tile_start_uv, mask_tile_uv_size);
    }
}

////////////////////////////  RESAMPLING FUNCTIONS  ////////////////////////////

vec3 downsample_vertical_sinc_tiled(const sampler2D texture,
    const vec2 tex_uv, const vec2 texture_size, const float dr,
    const float magnification_scale, const float tile_size_uv_r)
{
    //  Requires:   1.) dr == du == 1.0/texture_size.x or
    //                  dr == dv == 1.0/texture_size.y
    //                  (whichever direction we're resampling in).
    //                  It's a scalar to save register space.
    //              2.) tile_size_uv_r is the number of texels an input tile
    //                  takes up in the input texture, in the direction we're
    //                  resampling this pass.
    //              3.) magnification_scale must be <= 1.0.
    //  Returns:    Return a [Lanczos] sinc-resampled pixel of a vertically
    //              downsized input tile embedded in an input texture.  (The
    //              vertical version is special-cased though: It assumes the
    //              tile size equals the [static] texture size, since it's used
    //              on an LUT texture input containing one tile.  For more
    //              generic use, eliminate the "static" in the parameters.)
    //  The "r" in "dr," "tile_size_uv_r," etc. refers to the dimension
    //  we're resizing along, e.g. "dy" in this case.
    #ifdef USE_SINGLE_STATIC_LOOP
        //  A static loop can be faster, but it might blur too much from using
        //  more samples than it should.
        const int samples = int(max_sinc_resize_samples_m4);
    #else
        const int samples = int(get_dynamic_loop_size(magnification_scale));
    #endif

    //  Get the first sample location (scalar tile uv coord along the resized
    //  dimension) and distance from the output location (in texels):
    const float input_tiles_per_texture_r = 1.0/tile_size_uv_r;
    //  true = vertical resize:
    const vec2 first_texel_tile_r_and_dist = get_first_texel_tile_uv_and_dist(
        tex_uv, texture_size, dr, input_tiles_per_texture_r, samples, true);
    const vec4 first_texel_tile_uv_rrrr = first_texel_tile_r_and_dist.xxxx;
    const vec4 first_dist_unscaled = first_texel_tile_r_and_dist.yyyy;
    //  Get the tile sample offset:
    const float tile_dr = dr * input_tiles_per_texture_r;

    //  Sum up each weight and weighted sample color, varying the looping
    //  strategy based on our expected dynamic loop capabilities.  See the
    //  loop body macros above.
    int i_base = 0;
    vec4 weight_sum = vec4(0.0);
    vec3 pixel_color = vec3(0.0);
    const int i_step = 4;
    #ifdef BREAK_LOOPS_INTO_PIECES
        if(samples - i_base >= 64)
        {
            for(int i = 0; i < 64; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 64;
        }
        if(samples - i_base >= 32)
        {
            for(int i = 0; i < 32; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 32;
        }
        if(samples - i_base >= 16)
        {
            for(int i = 0; i < 16; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 16;
        }
        if(samples - i_base >= 8)
        {
            for(int i = 0; i < 8; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 8;
        }
        if(samples - i_base >= 4)
        {
            for(int i = 0; i < 4; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 4;
        }
        //  Do another 4-sample block for a total of 128 max samples.
        if(samples - i_base > 0)
        {
            for(int i = 0; i < 4; i += i_step)
            {
                VERTICAL_SINC_RESAMPLE_LOOP_BODY;
            }
        }
    #else
        for(int i = 0; i < samples; i += i_step)
        {
            VERTICAL_SINC_RESAMPLE_LOOP_BODY;
        }
    #endif
    //  Normalize so the weight_sum == 1.0, and return:
    const vec2 weight_sum_reduce = weight_sum.xy + weight_sum.zw;
    const vec3 scalar_weight_sum = vec3(weight_sum_reduce.x + 
        weight_sum_reduce.y);
    return (pixel_color/scalar_weight_sum);
}

vec3 downsample_horizontal_sinc_tiled(const sampler2D texture,
    const vec2 tex_uv, const vec2 texture_size, const float dr,
    const float magnification_scale, const float tile_size_uv_r)
{
    //  Differences from downsample_horizontal_sinc_tiled:
    //  1.) The dr and tile_size_uv_r parameters are not static consts.
    //  2.) The "vertical" parameter to get_first_texel_tile_uv_and_dist is
    //      set to false instead of true.
    //  3.) The horizontal version of the loop body is used.
    //  TODO: If we can get guaranteed compile-time dead code elimination,
    //  we can combine the vertical/horizontal downsampling functions by:
    //  1.) Add an extra static const bool parameter called "vertical."
    //  2.) Supply it with the result of get_first_texel_tile_uv_and_dist().
    //  3.) Use a conditional assignment in the loop body macro.  This is the
    //      tricky part: We DO NOT want to incur the extra conditional
    //      assignment in the inner loop at runtime!
    //  The "r" in "dr," "tile_size_uv_r," etc. refers to the dimension
    //  we're resizing along, e.g. "dx" in this case.
    #ifdef USE_SINGLE_STATIC_LOOP
        //  If we have to load all samples, we might as well use them.
        const int samples = int(max_sinc_resize_samples_m4);
    #else
        const int samples = int(get_dynamic_loop_size(magnification_scale));
    #endif

    //  Get the first sample location (scalar tile uv coord along resized
    //  dimension) and distance from the output location (in texels):
    const float input_tiles_per_texture_r = 1.0/tile_size_uv_r;
    //  false = horizontal resize:
    const vec2 first_texel_tile_r_and_dist = get_first_texel_tile_uv_and_dist(
        tex_uv, texture_size, dr, input_tiles_per_texture_r, samples, false);
    const vec4 first_texel_tile_uv_rrrr = first_texel_tile_r_and_dist.xxxx;
    const vec4 first_dist_unscaled = first_texel_tile_r_and_dist.yyyy;
    //  Get the tile sample offset:
    const float tile_dr = dr * input_tiles_per_texture_r;

    //  Sum up each weight and weighted sample color, varying the looping
    //  strategy based on our expected dynamic loop capabilities.  See the
    //  loop body macros above.
    int i_base = 0;
    vec4 weight_sum = vec4(0.0);
    vec3 pixel_color = vec3(0.0);
    const int i_step = 4;
    #ifdef BREAK_LOOPS_INTO_PIECES
        if(samples - i_base >= 64)
        {
            for(int i = 0; i < 64; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 64;
        }
        if(samples - i_base >= 32)
        {
            for(int i = 0; i < 32; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 32;
        }
        if(samples - i_base >= 16)
        {
            for(int i = 0; i < 16; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 16;
        }
        if(samples - i_base >= 8)
        {
            for(int i = 0; i < 8; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 8;
        }
        if(samples - i_base >= 4)
        {
            for(int i = 0; i < 4; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
            i_base += 4;
        }
        //  Do another 4-sample block for a total of 128 max samples.
        if(samples - i_base > 0)
        {
            for(int i = 0; i < 4; i += i_step)
            {
                HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
            }
        }
    #else
        for(int i = 0; i < samples; i += i_step)
        {
            HORIZONTAL_SINC_RESAMPLE_LOOP_BODY;
        }
    #endif
    //  Normalize so the weight_sum == 1.0, and return:
    const vec2 weight_sum_reduce = weight_sum.xy + weight_sum.zw;
    const vec3 scalar_weight_sum = vec3(weight_sum_reduce.x +
        weight_sum_reduce.y);
    return (pixel_color/scalar_weight_sum);
}

vec2 convert_phosphor_tile_uv_wrap_to_tex_uv(const vec2 tile_uv_wrap,
    const vec4 mask_tile_start_uv_and_size)
{
    //  Requires:   1.) tile_uv_wrap contains tile-relative uv coords, where the
    //                  tile spans from [0, 1], such that (0.5, 0.5) is at the
    //                  tile center.  The input coords can range from [0, inf],
    //                  and their fracttional parts map to a repeated tile.
    //                  ("Tile" can mean texture, the video embedded in the
    //                  texture, or some other "tile" embedded in a texture.)
    //              2.) mask_tile_start_uv_and_size.xy contains tex_uv coords
    //                  for the start of the embedded tile in the full texture.
    //              3.) mask_tile_start_uv_and_size.zw contains the [fracttional]
    //                  tex_uv size of the embedded tile in the full texture.
    //  Returns:    Return tex_uv coords (used for texture sampling)
    //              corresponding to tile_uv_wrap.
    if(params.mask_sample_mode_desired < 0.5)
    {
        //  Manually repeat the resized mask tile to fill the screen:
        //  First get fracttional tile_uv coords.  Using fract/fmod on coords
        //  confuses anisotropic filtering; fix it as user options dictate.
        //  derived-settings-and-constants.h disables incompatible options.
        #ifdef ANISOTROPIC_TILING_COMPAT_TILE_FLAT_TWICE
            vec2 tile_uv = fract(tile_uv_wrap * 0.5) * 2.0;
        #else
            vec2 tile_uv = fract(tile_uv_wrap);
        #endif
        #ifdef ANISOTROPIC_TILING_COMPAT_FIX_DISCONTINUITIES
            const vec2 tile_uv_dx = ddx(tile_uv);
            const vec2 tile_uv_dy = ddy(tile_uv);
            tile_uv = fix_tiling_discontinuities_normalized(tile_uv,
                tile_uv_dx, tile_uv_dy);
        #endif
        //  The tile is embedded in a padded FBO, and it may start at a
        //  nonzero offset if border texels are used to avoid artifacts:
        const vec2 mask_tex_uv = mask_tile_start_uv_and_size.xy +
            tile_uv * mask_tile_start_uv_and_size.zw;
        return mask_tex_uv;
    }
    else
    {
        //  Sample from the input phosphor mask texture with hardware tiling.
        //  If we're tiling at the original size (mode 2), the "tile" is the
        //  whole texture, and it contains a large number of triads mapped with
        //  a 1:1 pixel:texel ratio.  OTHERWISE, the texture contains a single
        //  unresized tile.  tile_uv_wrap already has correct coords for both!
        return tile_uv_wrap;
    }
}

#endif  //  PHOSPHOR_MASK_RESIZING_H

