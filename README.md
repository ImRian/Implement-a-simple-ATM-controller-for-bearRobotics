# Simple ATM Controller<hr>

### 개요<br>
이 프로젝트는 Python으로 구현된 간단한 ATM 컨트롤러입니다. 사용자는 카드를 삽입하고 PIN 번호를 입력한 뒤, 계좌를 선택하여 잔액을 확인하거나 입금 및 출금을 할 수 있습니다. 이 프로젝트는 실제 은행 시스템이나 ATM 하드웨어와 통합하지 않고, 기본적인 ATM 작동 흐름을 모의합니다.

### 설치 방법<br>
이 프로젝트를 로컬 시스템에 설치하려면 다음 단계를 따르세요:

GitHub에서 프로젝트를 클론합니다:
```bash
git clone https://github.com/ImRian/Implement-a-simple-ATM-controller-for-bearRobotics.git
```
클론된 디렉터리로 이동합니다:
```bash
cd Implement-a-simple-ATM-controller-for-bearRobotics
```
### 사용 방법
atm_controller.py 파일에는 ATMController 클래스가 정의되어 있으며, 이를 통해 ATM의 기본적인 작동 흐름을 시뮬레이션할 수 있습니다.

#### 예제 사용법은 다음과 같습니다:
```bash
from atm_controller import ATMController, BankSystem

# 은행 시스템과 ATM 컨트롤러 인스턴스 생성
bank_system = BankSystem()
atm_controller = ATMController(bank_system)

# 카드 삽입, PIN 번호 입력, 계정 선택, 잔액 확인 등의 작업 수행
account_number = '1234-5678'
atm_controller.insert_card(account_number)
if atm_controller.enter_pin('1111'):
    print("PIN 번호 확인 완료")
    balance = atm_controller.check_balance()
    print(f"현재 잔액: {balance}")
```

###  테스트 실행 방법 
이 프로젝트에는 unittest를 사용한 자동화된 테스트가 포함되어 있습니다. 테스트를 실행하려면 다음 명령을 사용하세요:
```bash
python -m unittest test_atm_controller.py
```
이 명령은 test_atm_controller.py 파일에 정의된 테스트 케이스를 실행합니다.

<hr>

### 기본 ATM 흐름 구현

**카드 삽입 (insert_card)**: 사용자가 카드(계좌 번호)를 삽입하는 동작을 시뮬레이션합니다.

**PIN 번호 입력 (enter_pin)**: 사용자로부터 PIN 번호를 입력받아, BankSystem의 verify_pin 메서드를 통해 해당 계좌의 PIN 번호와 일치하는지 확인합니다.

**계정 선택 (select_account)**: 사용자가 계정을 선택하는 동작을 시뮬레이션합니다. 실제로는 insert_card 메서드를 통해 이미 계정이 선택되었으나, 이 메서드는 향후 확장을 위해 포함되었습니다.

**잔액 확인/입금/출금 (check_balance, deposit, withdraw)**: 사용자가 계좌의 잔액을 확인하고, 돈을 입금하거나 출금하는 기능을 구현합니다.

###  단순화된 세계관
모든 계좌 잔액과 거래는 정수로 처리되어, 세계에서 1달러 지폐만 존재한다는 가정 하에 구현되었습니다.

### 실제 은행 시스템과의 통합 불필요
BankSystem 클래스는 실제 은행 시스템을 모의하는 간단한 형태로 구현되어, 은행 계좌 정보를 내부적으로 관리합니다.
실제 은행 API의 특정 기능(예: PIN 번호 확인)을 간단한 메서드로 시뮬레이션합니다.

### 테스트 코드 포함
test_atm_controller.py는 unittest 프레임워크를 사용하여 ATMController의 기능을 테스트합니다.
테스트 케이스는 카드 삽입, 잘못된 PIN 입력 후 올바른 PIN 입력, 잔액 확인, 입금, 출금 등의 프로세스를 검증합니다.
이는 코드가 예상대로 작동하는지 자동으로 확인하며, 향후 코드 수정 시 재사용할 수 있는 테스트를 제공합니다.

### 사용자 인터페이스 구현 용이성
본 코드는 함수/클래스/메서드 형태로 구현되어 있어, 다른 엔지니어가 사용자 인터페이스를 구현할 수 있는 충분한 기반을 제공합니다.
복잡한 실세계 문제 단순화

###  실제 ATM 시스템의 복잡한 요소들(예: 네트워크 통신, 다양한 화폐 단위 처리, 사용자 인터페이스 등)
이 프로젝트의 범위에서 제외되었습니다. 이는 문제의 핵심 요구사항에 집중하여 간단한 ATM 컨트롤러를 구현하고자 하는 목적을 반영합니다.

