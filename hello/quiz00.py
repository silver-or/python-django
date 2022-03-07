from hello import Member
from hello.domains import my100, myRandom, memberlist


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        op = ['+', '-', '*', '/', '%']
        opcode = op[myRandom(0, 4)]
        s = f'{a} {opcode} {b} = '
        if opcode == '+':
            s += f'{self.add(a, b)}'
        elif opcode == '-':
            s += f'{self.sub(a, b)}'
        elif opcode == '*':
            s += f'{self.mul(a, b)}'
        elif opcode == '/':
            s += f'{self.div(a, b)}'
        else:
            s += f'{self.mod(a, b)}'
        print(s)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = Quiz00.quiz06memberChoice(self)
        this.height = myRandom(160, 190)
        this.weight = myRandom(50, 100)
        bmi = this.weight / (this.height * this.height) * 10000
        s = f'{this.name}님의 비만도 결과 : '
        if bmi >= 35:
            s += '고도 비만'
        elif bmi >= 30:
            s += '중(重)도 비만 (2단계 비만)'
        elif bmi >= 25:
            s += '경도 비만 (1단계 비만)'
        elif bmi >= 23:
            s += '과체중'
        elif bmi >= 18.5:
            s += '정상'
        else:
            s += '저체중'
        print(s)

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        u = myRandom(1, 3)
        c = myRandom(1, 3)
        arr = ['가위', '바위', '보', 'Draw', 'Win', 'Lose']
        i = 3
        if abs(u - c) == 1:
            i = 4 if u > c else 5
        elif abs(u - c) == 2:
            i = 5 if u > c else 4
        print(f'user : {arr[u - 1]}, com : {arr[c - 1]} \n결과 : {arr[i]}')

    def quiz04leap(self):
        year = myRandom(1960, 2022)
        print(f'{year}년은 윤년입니다.' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else f'{year}년은 평년입니다.')

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        hap = self.hap(kor, eng, math)
        avg = self.avg(hap)
        grade = self.getGrade(avg)
        passChk = self.passChk(avg)
        print(f'국어 점수 : {kor}\n영어 점수 : {eng}\n수학 점수 : {math}\n합계 : {hap}\n평균 : {avg:.2f}\n학점 : {grade}\n합격 여부 : {passChk}')

    def hap(self, kor, eng, math):
        return kor + eng + math

    def avg(self, hap):
        return hap / 3.0

    def getGrade(self, avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def passChk(self, avg):  # 60점 이상 이면 합격
        return '합격' if avg >= 60 else '불합격'

    def quiz06memberChoice(self):
        return memberlist()[myRandom(0, 23)]

    def quiz07lotto(self):
        answer = []
        user = []
        count = 0
        while 1:
            anum = myRandom(1, 45)
            if anum not in answer:
                answer.append(anum)
            if len(answer) == 6:
                break
        while 1:
            unum = myRandom(1, 45)
            if unum not in user:
                user.append(unum)
            if len(user) == 6:
                break
        for i in range(6):
            if user[i] in answer:
                count += 1
        s = f'이번주 로또 당첨 번호 : {answer}\n사용자 번호 : {user}\n'
        if count == 6:
            s += '1등입니다.'
        elif count == 5:
            s += '2등입니다.'
        elif count == 4:
            s += '3등입니다.'
        else:
            s += '낙첨되었습니다.'
        print(s)

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()
        '''
        name = Quiz00.quiz06memberChoice(self)
        bal = 0
        while 1:
            menu = int(input('0. Exit\n1. 입금\n2. 출금\n'))
            if menu == 0:
                break
            elif menu == 1:
                money = myRandom(100, 10000)
                bal = self.deposit(bal, money)
            elif menu == 2:
                money = myRandom(100, 10000)
                bal = self.withdraw(bal, money)
            print(f'{name}님의 잔고 : {bal}') if bal is not None else print(f'{name}님의 잔고 : 0')

    def deposit(self, bal, money):
        if bal is not None:
            bal += money
        else:
            bal = money
        return bal

    def withdraw(self, bal, money):
        if bal is not None and bal >= money:
            bal -= money
        else:
            print('잔고가 부족합니다.')
        return bal
        '''

    def quiz09gugudan(self):  # 책받침구구단
        s = ''
        for k in range(2, 7, 4):
            for i in range(1, 10):
                for j in range(k, k + 4):
                    s += f'{j} * {i} = {i * j} \t'
                s += '\n'
            s += '\n'
        print(s)

'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 비트은행이다.
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
예를들면 123-12-123456 이다.
금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
'''


class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00.quiz06memberChoice(self) if name is None else name
        self.account_number = self.create_account_number() if account_number is None else account_number
        self.money = myRandom(100, 1000) if money is None else money

    def to_string(self):
        return f'은행 : {self.BANK_NAME}, ' \
                f'입금자 : {self.name}, ' \
                f'계좌번호 : {self.account_number}, ' \
                f'금액 : {self.money} 만원'

    def create_account_number(self):
        return ''.join('-' if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13))

    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. 종료 1. 계좌개설 2. 계좌목록 3. 입금 4. 출금 5. 계좌해지\n')
            if menu == '0':
                break
            elif menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} ... 개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join(i.to_string() for i in ls)
                print(a)
            elif menu == '3':
                account_number = input('입금할 계좌번호 : ')
                deposit = int(input('입금액 : '))
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        j.money += deposit
            elif menu == '4':
                account_number = input('출금할 계좌번호 : ')
                money = int(input('출금액 : '))
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        if j.money >= money:
                            j.money -= money
                        else:
                            print('잔고 부족')
            elif menu == '5':
                account_number = input('탈퇴할 계좌번호 : ')
                for i in ls:
                    i.del_account(ls, account_number)
            else:
                print('Wrong Number.. Try Again')
                continue

