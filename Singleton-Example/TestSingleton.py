from Logger import Logger

if __name__ == "__main__":
    print("--- Singleton Pattern Example ---")

    # Create the first logger instance
    logger1 = Logger()
    logger1.log("This is the first message.")

    # Create the second logger instance
    logger2 = Logger()
    logger2.log("This is the second message.")

    # Check if both instances are the same
    print(f"logger1 is logger2: {logger1 is logger2}")

    # Check if they share the same state (messages list)
    print("Messages in logger1:", logger1.messages)
    print("Messages in logger2:", logger2.messages)

    # Assertions for verification
    if logger1 is logger2:
        print("SUCCESS: Both variables refer to the same object.")
    else:
        print("FAILURE: Variables refer to different objects.")

    if len(logger1.messages) == 2 and len(logger2.messages) == 2:
        print("SUCCESS: State is shared between usages.")
    else:
        print("FAILURE: State is not shared correctly.")
