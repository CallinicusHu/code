import room_ex45
import room_1_ex45
import room_2_ex45
import room_3_ex45
import room_4_ex45
import walk_ex45
import layout_ex45

room_1 = room_1_ex45.Room_1()
room_2 = room_2_ex45.Room_2()
room_3 = room_3_ex45.Room_3()
room_4 = room_4_ex45.Room_4()

ROOMS = {1: room_1, 2: room_2, 3: room_3, 4: room_4}

game = walk_ex45.RunTheGame(ROOMS)
game.play()