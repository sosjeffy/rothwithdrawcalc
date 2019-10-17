# Formula for compound interest is total = principle(1+(rate/compounding freq))^(compound freq * time)


def _get_num() -> int:
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print("Sorry, that is not a valid age.")
            continue
    return num


def _calc(sAmt, sAge, sEnd, sWith, withAmt, rate) -> float:
    r = rate/100
    currentAmt = sAmt*((1+(r/1))**(1*(sEnd - sWith)))

    withPerYr = withAmt*12

    for i in range(sEnd - sWith):
        currentAmt = (currentAmt-withPerYr) * (1+(r/1))**(1*1)

    return currentAmt


if __name__ == "__main__":
    print("How much money would you like your IRA to start with? (whole number only): ", end='')
    startAmount = _get_num()
    print()

    print("Let's get the age at which you first put money into your IRA: ", end='')
    startAge = _get_num()
    print()

    print("Now, let's get the age at which you want to check your total balance: ", end='')
    endAge = _get_num()
    print()

    print("Ok, at what age would you like to start withdrawing?: ", end='')
    startWithdrawal = _get_num()
    print()

    print("Great! How much would you like to withdraw per month? (whole number only): ", end='')
    withdrawalAmount = _get_num()
    print()

    print("Finally, what percentage do you expect to earn annually? (whole number only): ", end='')
    rate = _get_num()
    print()

    print(f'Starting with a principle of ${startAmount} and '
          f'monthly withdrawal of ${withdrawalAmount} at {rate}% annually,'
          f' your FINAL balance at age {endAge} will be '
          f'${_calc(startAmount, startAge, endAge, startWithdrawal,withdrawalAmount, rate):,.2f}')