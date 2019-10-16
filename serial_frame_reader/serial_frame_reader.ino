/*
  Serial Frame Reader

  Receives images over serial and draws them to neopixels.
  An example of an image transmission:
    [             this byte starts the frame
    >             this byte starts a pixel. The three color bytes must follow
    0x05          red value
    0x88          green value
    0xFF          blue value
    >***          the next pixel
    .             this byte specifies that 64 pixels will follow
    rgbrgbrgb...  64 pixels' worth of rgb data
    ]             this byte ends the frame and has the arduino update the display

  You can also send 'x' to clear the image buffer

  created 17 July 2019
  by Chris Raff
*/

#define FASTLED_ALLOW_INTERRUPTS 0
#include <FastLED.h>

// pin 2 is D4 on Wemos D1 mini
#define LED_PIN 2
#define NUM_LEDS 64

CRGB leds[NUM_LEDS];


unsigned int framePixel = 0;


void setup() {
  Serial.begin(115200);

  FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);

  // This prevents your USB port from being damaged, you can change this depending on your power configuration
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);

  FastLED.clear();
  FastLED.show();
}


void loop() {
  while (Serial.available()) {

    byte head = Serial.read();

    switch (head) {
    case '[': // frame start
      framePixel = 0;
      break;

    case ']': // frame end
      FastLED.show();
      break;

    case '>': // pixel (data length: 3 bytes)
    {
      // If the byte isn't available yet, reading it will result in
      // a value of 255 and then future data will be misaligned
      while (!Serial.available()) {}
      byte r = Serial.read();
      while (!Serial.available()) {}
      byte g = Serial.read();
      while (!Serial.available()) {}
      byte b = Serial.read();

      if (framePixel < NUM_LEDS) {
        leds[framePixel] = CRGB(r,g,b);
      }

      framePixel++;

      break;
    }

    case '.': // 64 pixels (data length: 192 bytes)
    {
      for (byte i = 0; i < 64; i++) {
        while (!Serial.available()) {}
        byte r = Serial.read();
        while (!Serial.available()) {}
        byte g = Serial.read();
        while (!Serial.available()) {}
        byte b = Serial.read();

        if (framePixel < NUM_LEDS) {
          leds[framePixel] = CRGB(r,g,b);
        }

        framePixel++;
      }

      break;
    }

    case 'x': // clear image buffer
    {
      FastLED.clear();
    }

    default:
    { /* unknown character, do nothing */ }

    } // end of switch (head)

    yield;
  } // end of while (Serial.available())
}
