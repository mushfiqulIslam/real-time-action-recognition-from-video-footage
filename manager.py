from tools.train_val_test_spliter import split


def manage():
    print("------------------------")
    split()
    print("------------------------")


if __name__ == "__main__":
    print("Starting the Project")
    try:
        manage()
    except Exception as e:
        print(e)
