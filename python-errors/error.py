def main():
    num_fizz = input("How long should we calculate fizzbuzz for? ")
    try: 
        num_fizz = int(num_fizz)
    except:
        print ("Sorry I can't do that Dave")
    else:
        fizzBuzz(num_fizz)
    finally:
        print("Goodbye!")


def fizzBuzz(int):
    fizzBuzzNums = {
        2: "fizz",
        5: "buzz"
    }
    for i in range (1, int + 1):
        found = 0
        for j in fizzBuzzNums:
            if i % j == 0:
                print (fizzBuzzNums[j], end = "")
                found = 1
        if found == 1:
            print("")
        else:
            print(i)

if __name__ == "__main__":
    main()
