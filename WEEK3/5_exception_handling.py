def input_func(idx):
    try:
        # print("idx is", idx)
        my_lst = [1, 2, 3]
        return my_lst[idx]
    except Exception as e:
        print(e)
        return -1

def  main():
    var1 = 2
    var2 = 4

    if var1 > 3:
        raise Exception("The var value is more than 3. Value provided: {}".format(var1))

    # AssertionError
    assert (var2 > 3), "The variable var is less than 3"
    # try except
    try:
        assert (var2 > 3), "The variable var is less than 3"
        zero_val = 12/0
    except AssertionError as ae:
        print("Error Caught:", ae)
    except ZeroDivisionError as ze:
        print("Error Caught:", ze)
    else:
        print("Reached here because there were no exception")
        try:
            a = 4
            b = 5
            c = a + b
        except Exception as ex:
            print(ex)
        finally:
            print("This block will be called at the end")

        try:
            my_lst = [1, 2, 3]
            print(my_lst[100])
        except IndexError as ie:
            print(ie)
        except LookupError as le:
            print(le)
        except Exception as e:
            print(e)
        """
        except AssertionError as ae:
            print("error caought:", ae)
        except ZeroDivisionError as ze:
            print("error caught:", ze)
        except Exception as e:
            print("error caught", e)
          """

    while True:
        idx = input("enter a value")
        idx = int(idx)
        ret_val = input_func(idx)
        print("ret_val is", ret_val)
        if ret_val == -1:
            print("index was out of bonds. Please enter again a number less than 3 and greater than -1")
        else:


if __name__ == "__main__":
    main()