// подставь свои сигналы пульта
#define IR_LEFT 0x10
#define IR_OK   0x38
#define IR_RIGHT 0x5A
#define IR_DOWN 0x4A
#define IR_UP 0x18

#include <NecDecoder.h>
NecDecoder ir;

void setup() {
    Serial.begin(9600);
    // подключил на D2, прерывание 0
    attachInterrupt(0, irIsr, FALLING);
}
// в прерывании вызываем tick()
void irIsr() {
    ir.tick();
}

void loop() {
    if (ir.available()) {
        switch (ir.readCommand()) {
            case IR_UP:
                Serial.println("IR_UP");
                break;
            case IR_LEFT:
                Serial.println("IR_LEFT");
                break;
            case IR_OK:
                Serial.println("IR_OK");
                break;
            case IR_RIGHT:
                Serial.println("IR_RIGHT");
                break;
            case IR_DOWN:
                Serial.println("IR_DOWN");
                break;
        }
    }
}
