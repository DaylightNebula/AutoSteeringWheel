import pyvjoy
import mouse

j = pyvjoy.VJoyDevice(1)

wheel_value = 0  # -32768 -> 32767
while True:
    #print("mouse wheel: " + str(mouse.get_position()))
    wheel_value = (mouse.get_position()[0] / 1920) * 32790
    #if wheel_value > 32767: wheel_value = 32767
    print("wheel value: " + str(wheel_value))
    j.set_axis(pyvjoy.HID_USAGE_Y, int(wheel_value))
    #j.update()
