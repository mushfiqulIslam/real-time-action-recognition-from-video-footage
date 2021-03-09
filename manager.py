from train_val_test_spliter import split
def manage():
    print("------------------------")
    split()
    print("------------------------")
    pass
if __name__ == "__main__":
    print("Staring to Run the Project")
    try:
        manage()
    except Exception as e:
        print(e)
