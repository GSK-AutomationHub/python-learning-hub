# if elif else

# problem statement: validate person eligibility for voting


def voter_eligibility_check():
    name = input("please enter your firstname: ")
    age = int(input("please enter your running age: "))

    if age >= 18:
        print(f'Hello {name}, congratulations you are eligible for voting!')
        voter_kyc_check(1)
    else:
        print(f'Hello {name}, you are not eligible to vote this year since underage')
        voter_kyc_check(0)


def voter_kyc_check(is_eliigible):
    if is_eliigible:
        adhar_no = input("please enter your adhar card no: ")
        if len(adhar_no) == 14:
            print("Thanks, your KYC details matched")
        else:
            print("Your KYC details not matching with our record, please check with booth manager")
    else:
        print("Sorry, your kyc is not yet updated with our system")


voter_eligibility_check()

