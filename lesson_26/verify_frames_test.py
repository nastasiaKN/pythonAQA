from frame_helpers import handle_frame

def test_frame1_verification(driver):
    handle_frame(driver, "frame1", "input1", "Frame1_Secret")

def test_frame2_verification(driver):
    handle_frame(driver, "frame2", "input2", "Frame2_Secret")