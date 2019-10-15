#define FASTLED_ALLOW_INTERRUPTS 0
#include <FastLED.h>

// pins for Wemos d1 mini
#define DATA 0  // D3
#define WIDTH 8
#define HEIGHT 8
#define NUM_LEDS WIDTH*HEIGHT

CRGB leds[NUM_LEDS];


// -------------------------
void setup() {
  Serial.begin(115200);

  FastLED.addLeds<WS2812B, DATA, GRB>(leds, 0, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 1500);
  FastLED.setCorrection( TypicalLEDStrip );
  FastLED.setBrightness(128);
}


void loop() {
  // READ IN NEW MESSAGES FROM SERIAL
  if(Serial.available() > NUM_LEDS+1) {
    while(Serial.available() > NUM_LEDS+1) {
      Serial.read();
    }
  }
  if(Serial.available() == NUM_LEDS+1) {
    byte color_channel = Serial.read();
    for (int i = 0; i < NUM_LEDS && Serial.available() > 0; i++) {
      if(color_channel == 0) {
        leds[i].r = Serial.read();
      }
      else if(color_channel == 1) {
        leds[i].g = Serial.read();
      }
      else if(color_channel == 2) {
        leds[i].b = Serial.read();
      }
    }
    FastLED.show();
  }
}
