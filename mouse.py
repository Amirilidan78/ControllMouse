from pynput.mouse import Button, Controller

# make object to controll Mouse
mouse = Controller()
# Print Mouse Possition
print(mouse.position)
# set possition
mouse.position = (10, 20)
# move Mouse
mouse.move(5, -5)
# left click
mouse.press(Button.left)
mouse.release(Button.left)
# right click
mouse.press(Button.right)
mouse.release(Button.right)
# double click
mouse.click(Button.left, 2)

# multiple click
mouse.click(Button.left, 4)
