#pragma parameter target_gamma "Target Gamma" 2.2 0.1 5.0 0.1
#pragma parameter monitor_gamma "Monitor Gamma" 2.2 0.1 5.0 0.1
#pragma parameter overscan_percent_x "Horizontal Overscan %" 0.0 -25.0 25.0 1.0
#pragma parameter overscan_percent_y "Vertical Overscan %" 0.0 -25.0 25.0 1.0
#pragma parameter saturation "Saturation" 1.0 0.0 2.0 0.01
#pragma parameter contrast "Contrast" 1.0 0.0 10.0 0.05
#pragma parameter luminance "Luminance" 1.0 0.0 2.0 0.01
#pragma parameter black_level "Black Level" 0.00 -0.30 0.30 0.01
#pragma parameter bright_boost "Brightness Boost" 0.0 -1.0 1.0 0.05
#pragma parameter R "Red Channel" 1.0 0.0 2.0 0.05
#pragma parameter G "Green Channel" 1.0 0.0 2.0 0.05
#pragma parameter B "Blue Channel" 1.0 0.0 2.0 0.05
#pragma parameter ZOOM "Zoom Factor" 1.0 0.0 4.0 0.01
#pragma parameter XPOS "X Modifier" 0.0 -2.0 2.0 0.005
#pragma parameter YPOS "Y Modifier" 0.0 -2.0 2.0 0.005
#pragma parameter V_OSMASK "Overscan Mask Y" 0.0 0.0 1.0 0.005
#pragma parameter H_OSMASK "Overscan Mask X" 0.0 0.0 1.0 0.005

#if defined(VERTEX)

#if __VERSION__ >= 130
#define COMPAT_VARYING out
#define COMPAT_ATTRIBUTE in
#define COMPAT_TEXTURE texture
#else
#define COMPAT_VARYING varying 
#define COMPAT_ATTRIBUTE attribute 
#define COMPAT_TEXTURE texture2D
#endif

#ifdef GL_ES
#define COMPAT_PRECISION mediump
#else
#define COMPAT_PRECISION
#endif
COMPAT_VARYING     vec4 _color1;
COMPAT_VARYING     float _frame_rotation;
struct input_dummy {
    vec2 _video_size;
    vec2 _texture_size;
    vec2 _output_dummy_size;
    float _frame_count;
    float _frame_direction;
    float _frame_rotation;
};
struct output_dummy {
    vec4 _color1;
};
vec4 _oPosition1;
input_dummy _IN1;
vec4 _r0006;
COMPAT_ATTRIBUTE vec4 VertexCoord;
COMPAT_ATTRIBUTE vec4 COLOR;
COMPAT_ATTRIBUTE vec4 TexCoord;
COMPAT_VARYING vec4 COL0;
COMPAT_VARYING vec4 TEX0;
 
uniform mat4 MVPMatrix;
uniform int FrameDirection;
uniform int FrameCount;
uniform COMPAT_PRECISION vec2 OutputSize;
uniform COMPAT_PRECISION vec2 TextureSize;
uniform COMPAT_PRECISION vec2 InputSize;

#ifdef PARAMETER_UNIFORM
uniform COMPAT_PRECISION float target_gamma;
uniform COMPAT_PRECISION float monitor_gamma;
uniform COMPAT_PRECISION float overscan_percent_x;
uniform COMPAT_PRECISION float overscan_percent_y;
uniform COMPAT_PRECISION float saturation;
uniform COMPAT_PRECISION float contrast;
uniform COMPAT_PRECISION float luminance;
uniform COMPAT_PRECISION float black_level;
uniform COMPAT_PRECISION float bright_boost;
uniform COMPAT_PRECISION float R;
uniform COMPAT_PRECISION float G;
uniform COMPAT_PRECISION float B;
uniform COMPAT_PRECISION float ZOOM;
uniform COMPAT_PRECISION float XPOS;
uniform COMPAT_PRECISION float YPOS;
uniform COMPAT_PRECISION float V_OSMASK;
uniform COMPAT_PRECISION float H_OSMASK;
#else
#define overscan_percent_x 0.0         // crop width of image by X%; default is 0.0
#define overscan_percent_y 0.0         // crop height of image by X%; default is 0.0
#define saturation 1.0                 // color saturation; default 1.0
#define monitor_gamma 2.2              // gamma setting of your current display; LCD monitors typically have a gamma of 2.2
#define target_gamma 2.2               // the gamma you want the image to have; CRT TVs typically have a gamma of 2.4
#define contrast 1.0                   // image contrast; default 1.0
#define luminance 1.0                  // image luminance; default 1.0
#define black_level 0.0
#define bright_boost 0.0               // adds to the total brightness. Negative values decrease it; Use values between 1.0 (totally white) and -1.0 (totally black); default is 0.0
#define R 1.0
#define G 1.0
#define B 1.0
#define ZOOM 1.0
#define XPOS 0.0
#define YPOS 0.0
#define V_OSMASK 0.0
#define H_OSMASK 0.0
#endif

void main()
{
    vec4 _oColor;
    vec2 _otexCoord;
    vec2 _shift;
    vec2 _overscan_coord;
    _r0006 = VertexCoord.x*MVPMatrix[0];
    _r0006 = _r0006 + VertexCoord.y*MVPMatrix[1];
    _r0006 = _r0006 + VertexCoord.z*MVPMatrix[2];
    _r0006 = _r0006 + VertexCoord.w*MVPMatrix[3];
    _oPosition1 = _r0006;
    _oColor = COLOR;
    _shift = (5.00000000E-01*InputSize)/TextureSize;
    _overscan_coord = ((TexCoord.xy - _shift) / ZOOM) * (1.0 - vec2(overscan_percent_x / 100.0, overscan_percent_y / 100.0)) + _shift;
    _otexCoord = _overscan_coord;
    gl_Position = _r0006;
    COL0 = COLOR;
    TEX0.xy = _overscan_coord + vec2(XPOS, YPOS);
} 
#elif defined(FRAGMENT)

#if __VERSION__ >= 130
#define COMPAT_VARYING in
#define COMPAT_TEXTURE texture
out vec4 FragColor;
#else
#define COMPAT_VARYING varying
#define FragColor gl_FragColor
#define COMPAT_TEXTURE texture2D
#endif

#ifdef GL_ES
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
#define COMPAT_PRECISION mediump
#else
#define COMPAT_PRECISION
#endif
COMPAT_VARYING     vec4 _color;
COMPAT_VARYING     float _frame_rotation;
struct input_dummy {
    vec2 _video_size;
    vec2 _texture_size;
    vec2 _output_dummy_size;
    float _frame_count;
    float _frame_direction;
    float _frame_rotation;
};
struct output_dummy {
    vec4 _color;
};
vec4 _ret_0;
vec3 _TMP5;
float _TMP4;
float _TMP3;
float _TMP2;
float _TMP1;
vec4 _TMP0;
uniform sampler2D Texture;
input_dummy _IN1;
vec3 _TMP29;
COMPAT_VARYING vec4 TEX0;

#ifdef PARAMETER_UNIFORM
uniform COMPAT_PRECISION float target_gamma;
uniform COMPAT_PRECISION float monitor_gamma;
uniform COMPAT_PRECISION float overscan_percent_x;
uniform COMPAT_PRECISION float overscan_percent_y;
uniform COMPAT_PRECISION float saturation;
uniform COMPAT_PRECISION float contrast;
uniform COMPAT_PRECISION float luminance;
uniform COMPAT_PRECISION float black_level;
uniform COMPAT_PRECISION float bright_boost;
uniform COMPAT_PRECISION float R;
uniform COMPAT_PRECISION float G;
uniform COMPAT_PRECISION float B;
uniform COMPAT_PRECISION float ZOOM;
uniform COMPAT_PRECISION float XPOS;
uniform COMPAT_PRECISION float YPOS;
uniform COMPAT_PRECISION float V_OSMASK;
uniform COMPAT_PRECISION float H_OSMASK;
#endif

vec3 grayscale(vec3 col)
{
   // ATSC grayscale standard
   return vec3(dot(col, vec3(0.2126, 0.7152, 0.0722)));
}

vec3 rgb2hsv(vec3 c)
{
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = c.g < c.b ? vec4(c.bg, K.wz) : vec4(c.gb, K.xy);
    vec4 q = c.r < p.x ? vec4(p.xyw, c.r) : vec4(c.r, p.yzx);

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}
 
uniform int FrameDirection;
uniform int FrameCount;
uniform COMPAT_PRECISION vec2 OutputSize;
uniform COMPAT_PRECISION vec2 TextureSize;
uniform COMPAT_PRECISION vec2 InputSize;
void main()
{
    vec2 fragcoord;
    vec3 res;
	vec3 gamma;
	vec3 satColor;
	vec3 conColor;

    fragcoord = TEX0.xy*(TextureSize.xy/InputSize.xy);
    res = COMPAT_TEXTURE(Texture, TEX0.xy).rgb;
	gamma = vec3(monitor_gamma / target_gamma); // setup ratio of display's gamma vs desired gamma
	
//saturation and luminance
   satColor = clamp(hsv2rgb(rgb2hsv(res) * vec3(1.0, saturation, luminance)), 0.0, 1.0);

//contrast and brightness
   conColor = clamp((satColor - 0.5) * contrast + 0.5 + bright_boost, 0.0, 1.0);
   
   conColor -= vec3(black_level); // apply black level
   conColor *= (vec3(1.0) / vec3(1.0-black_level));
   conColor = pow(conColor, vec3(1.0) / vec3(gamma)); // Apply gamma correction
	conColor *= vec3(R, G, B); // apply color channel adjustment

    if (fragcoord.y > V_OSMASK && fragcoord.y < (1.00000000E+00 - V_OSMASK)) { 
    } else {
        conColor = vec3( 0.00000000E+00, 0.00000000E+00, 0.00000000E+00);
    } 
    if (fragcoord.x > H_OSMASK && fragcoord.x < (1.00000000E+00 - H_OSMASK)) { 
    } else {
        conColor = vec3( 0.00000000E+00, 0.00000000E+00, 0.00000000E+00);
    } 
    _ret_0 = vec4(conColor.x, conColor.y, conColor.z, 1.00000000E+00);
    FragColor = _ret_0;
    return;
} 
#endif
