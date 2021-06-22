users = {}
while True :
    print("--------------")
    print("1 : 가입")
    print("2 : 탈퇴")
    print("3 : 비밀번호 변경하기")
    print("4 : 종료")
    s = input("선택 : ")
    if s == '4' :
        break
    if s == '1' :
        while True :
            id = input("새 아이디 : ")
            if id not in users :
                break
            print(id, "이미 존재")
        pword = input("패스워드 : ")
        users[id] = pword
        print(users)
    if s == '2' :
        while True :
            id = input("아이디 : ")
            if id in users :
                break
            print(id, "존재하지 않음")
        del users[id]
        print(users)
    if s == '3' :
        while True :
            id = input("아이디 : ")
            if id in users :
                break
            print(id, "존재하지 않음")
        pword = input("새 패스워드 : ")
        users[id] = pword
        print(users)

print(users)
         
            
        
