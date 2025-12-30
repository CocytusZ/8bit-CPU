from PIN_DEF import * 

fetch = [
    PC_OUT | MAR_IN,
    RAM_OUT | IR_IN | PC_INC,
    PC_OUT | MAR_IN,
    RAM_OUT | SRC_IN | PC_INC,
    PC_OUT | MAR_IN,
    RAM_OUT | DST_IN | PC_INC,
]