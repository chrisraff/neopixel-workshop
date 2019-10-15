#define FASTLED_ALLOW_INTERRUPTS 0
#include <FastLED.h>

// ---USED FOR LEDS---
//// pins for Arduino Nano ATmega328P (Old Bootloader)
//#define DATA 3  // D3
//#define NUM_LEDS 226

// pins for Wemos d1 mini
#define DATA 0  // D3
#define NUM_LEDS 226

CRGB leds[NUM_LEDS];


void setColor(byte r, byte g, byte b) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[ i ] = CRGB(r, g, b);
  }
  FastLED.show();
}

// -------------------------
void setup() {
  Serial.begin(115200);

  FastLED.addLeds<WS2812B, DATA, GRB>(leds, 0, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 1500);
  FastLED.setCorrection( TypicalLEDStrip );
//  FastLED.setBrightness(128);
}


void loop() {
  // READ IN NEW MESSAGES FROM SERIAL
  if(Serial.available() > 227) {
    while(Serial.available() > 227) {
      Serial.read();
    }
  }
  if(Serial.available() == 227) {
    byte color_channel = Serial.read();
    for (int i = 0; i < 226 && Serial.available() > 0; i++) {
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
