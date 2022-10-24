# Digital-mid

- 영상이란? : 가시광선을 센싱하여 자연 세계의 광학 현상을 2차원 이상의 데이터로 표현한 것
- 인식이란? : 3차원 공간에 존재하는 빛이 눈으로 입력되어 뇌가 인지하는 모든 과정
- 영상처리 : 획득장치(카메라)를 통해 획득한 영상을 `처리 / 해석 / 인식`하는 모든 분야를 의미
- 영상처리 기본단위 : 화소
- 디지털 영상이란? : 움직이는 시각적 이미지를 전자적 방식에 의해 표현한 것
- MFC(Microsoft Foundation Class)
- openCV :  컴퓨터 비전 라이브러리 중 하나로 이미지 프로세싱에 중점을 둔 라이브러리이다.
- 디지털 영상처리의 장점(4가지) : `취득 용이`, `처리 용이`, `재현 용이`, `저장 용이`
- 디지털 영상처리의 단점(1가지) : `데이터 손실`
- 사진영상(아날로그) : 물체에 반사되는 빛 신호(아날로그)를 표현
- 디지털영상(디지털) : 사진영상 → 디지털 신호로 변환 → 디지털 영상
- 디지털 신호의 장점(아날로그에 비해)
    - 아날로그 영상보다 화질이 우수하다.
    - 컴퓨터 기술의 발전을 그대로 반영하였다.
    - 영구적으로 데이터를 저장할 수 있다.
    - 데이터 통신 분야에서도 디지털 영상 전송을 가능케 했다.
- 디스플레이에서 영상을 보기까지의 단계
    - 아날로그 영상 취득 → 시공간 샘플링 → 영상처리 → 디스플레이 출력
    - 디지털 영상 취득 → 영상처리 → 디스플레이 출력
- 디지털 영상처리 기술(6가지) : `개선`, `복원`, `변환`, `분석`, `인식`, `압축`
- 디지털 영상처리 알고리즘(4가지) : `화소 점 처리`, `영역 처리`, `기하학적 처리`, `프레임 처리`

|                      입력 \ 출력 | 영상 | 심볼 |
| --- | --- | --- |
| 영상 | 영상처리 | 컴퓨터 비젼 |
| 심볼 | 컴퓨터 그래픽 | AI |

---

- `개선` : 영상을 **주관적으로** 향상 시키는 기술 / 인간이 보기 좋은 화질로 변환 / 응용하려는 목적에 맞게 변환
    - 평활화(Equalization), 첨예화(Sharpening), 잡음제거
- `복원` : 훼손 / 왜곡된 디지털 영상을 본래의 영상과 가장 가까운 형태로 복원하는 것
- `변환` : 디지털 영상의 데이터를 다른 형태의 데이터로 변환하는 작업(ex.밝기와 색의 크기 정보 → 밝기와 색의 크기 변화량)
    - 푸리에 변환, 이산 코사인 변환, 웨이브렛 변환
- `분석` : 영상이 지닌 속성을 수치화하여 표현 / `추출된 특징만으로는 원 영상으로 복원 불가`
    - 윤곽선 검출
- `인식` : 영상입력 → 전처리 → 영상 분할 → 특징추출 → 인식 (5단계)
    - 지문인식
- `압축` : 영상 데이터를 효율적으로 표현하여 저장 및 전송 효율성 최대화 / 부호화, 복호화 과정으로 구성
    - **손실압축** : 부호화, 복호화시 데이터 손실 발생(이후 복원시 원본과 다름)
    - **무손실압축** : 부호화, 복호화시 데이터 손실X(이후 복원시 원본과 같음)

---

- `화소 점 처리` : 화소 점의 원래 값이나 위치를 기반으로 화소 값 변경
    - 히스토그램, 명도 변환, 밝기 변환
- `영역 처리` : 화소의 원래 값과 이웃하는 화소의 값을 기반으로 화소 값 변경
    - 블러링(흐리게 만드는 것), 샤프닝(상세한 부분을 더욱 강조해 대비 효과를 내게 만드는 것)
- `기하학 처리` : 화소들의 위치를 변경
    - 스케일, 회전, 이동
- `프레임 처리` : 두 개 이상의 서로 다른 디지털 영상들로 새로운 화소 값 생성
    - AND / OR Operator

---

- 디지털 영상처리 시스템 : 아날로그 영상 → 디지털 영상으로 바꾸는 일련의 과정을 수행하는 시스템
- 디지털 영상처리 활용 분야
    - TV, 재생장치(**영상처리 활용 분야 중 가장 많은 생산량**) : 개선, 복원, 변환
    - 디지털 카메라 : 개선, 복원, 분석(얼굴 검출)
    - 지문, 얼굴, 홍채 : 인식
    - 차량 번호 : 인식
    - 문자 : 복원, 분석, 인식(OCR) 결합
    - 의료 영상 기술 : 초음파, MRI, CT, PET
    - **머신 비전(Machine Vision)** : 산업용 카메라가 생산된 제품의 품질 검사 & 모니터링
    - Interactive Game : NUI(Natural User Interface), 사용자 움직임을 입력으로 사용
- 모핑 : 변형(Metamorphosis)라는 말에서 유래된 기술 / 하나의 디지털 영상을 다른 디지털 영상으로 변환하는 효과

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled.png)

- 워핑 : 입력 영상의 크기, 길이, 두께 등의 형태를 변형하는 기술

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%201.png)

---

- 빛 : 사람이 볼 수 있는 일정 범위의 전자기파
    - 좁은 의미의 빛 : 가시광선(인간이 볼 수 있는 빛의 영역)
    - 넓은 의미의 빛 : 전자기파 전체
- 파장 짧 → 긴 순서대로 : r선 x선 자기장 가시광선(보라색→빨간색) 적외선 마이크로파
- 눈의구조(눈의 민감도 : 밝기 >>>>> 색상)
    - 각막 : 안구 보호 / 눈으로 들어오는 광선의 초기 초점을 형성
    - 홍채 : 빛의 양 조절
    - 수정체 : 상을 망막에 맺게 하는 볼록 렌즈, 초점 길이 조절
    - 망막 : 영상을 감지하는 기관, 간상세포/원추세포 분포
        - 간상세포 : 1억개, 밝기 민감, 색 구분 잘 못함, 밝기 정보를 시신경으로 전송
        - 원추세포 : 600만개, 색 구분 잘함, 세 종류의 시색소가 색에따라 다르게 반응, 색상정보를 시신경으로 전송
    - 황반 : 망막에서 가장 깊이 들어간 곳에 있음

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%202.png)

- 인간이 색을 인지하기 위한 3요소 : 광원, 물체, 눈
    - 광원 : 가시광선에서 각 파장의 빛의 양에 따라 색이 결정
    - 물체 : 파장의 반사계수에 따라 반사
    - 눈 : 물체에서 반사된 빛을 인지

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%203.png)

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%204.png)

- I(λ)는 인간의 눈에따라 다른 응답 특성을 가진다.
- 인식(3단계) : 3차원 공간에 존재하는 빛이 눈으로 입력되어 뇌가 인지하는 모든 과정
    - 감각 단계 : 외부 빛이 눈의 렌즈를 통해 망막의 신경 세포에서 전기적 신호로 변환 후 신경계를 통해 뇌로 보내지는 단계
    - 선택 단계 : 보고자 하는 대상을 분리하는 단계
    - 지각 단계 : 기억 데이터를 근거로 대상을 이해하여 지각하는 단계
- 디지털 영상처리
    - 저수준 영상처리 : 디지털 영상 획득, 포맷에 맞춰 저장
    - 중간 수준 영상처리 : 영상 분할, 심볼 매핑 등 특별 목적에 따라 영상을 가공하는 과정
    - 고수준 영상처리 : 영상 해석, 영상 인식
- 빛의 3속성 : 색상, 채도, 명도(교수님 자료 : 색상, 채도, 밝기)
- 디지털 영상의 구분
    - 흑백 디지털 영상 : 이진 영상(흰, 검) / 그레이 레벨 영상(흰, 검, 회)(명도로만 영상을 표현)
    - 컬러 디지털 영상 : 색 정보를 색상(Hue), 채도(Saturation), 명도(Intensity)의 3가지로 인식 / 색상 + 채도 = 색도(Chromaticity)
        - 색상 : 우리 눈에 비춰진 색의 느낌
        - 채도 : 색상의 선명함(빨간색 → 채도 높다, 분홍색 → 채도 낮다)
        - 명도(I) : 빛의 밝음 어두움(`흰색, 회색, 검정색은 색상이 없고 명도로만 나타냄`)
            - 명암 대비(Contrast) : 명도의 관계를 나타내며 가장 어두운 영역에서 가장 밝은 영역까지의 범위를 나타낸다.
            
            $$
            대비(Contrast) = (Imax - Imin) / (Imax + Imin)
            $$
            
- 인간의 지각 작용이 단순한 명도보다는 **명도의 대비(Contrast)**에 더 민감하다.
- 동시적 대비 : 명도의 느낌이 배경의 명도에 크게 의존한다.

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%205.png)

![위 그림 보고 이해할 줄 알아야 함](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%206.png)

위 그림 보고 이해할 줄 알아야 함

---

- `컬러 모델` : 색의 특징을 설명하기 위한 수학적 방법, 완벽한 컬러모델은 불가능 하다
    - RGB, CMYK, HSI, YCbCr
- `RGB` : 빛의 3원색(R, G, B) 이용, 가산체계(색을 혼합할수록 색상이 밝아짐)
    - RGB 컬러 모델을 사용하는 기계 : 모니터, TV
    - 스크린 안쪽의 전자총 갯수 : 3개
    - 각 성분(R, G, B)들은 동일한 비트 심도(depth)로 구성
    - R - 8bit라면, G, B도 각 8bit여서 컬러 영상은 24bit가 된다.

![그래픽 소프트웨어에서는 0~255로 표현(NOT 0 or 1)](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%207.png)

그래픽 소프트웨어에서는 0~255로 표현(NOT 0 or 1)

---

- `CMY` : C(청록색), M(자홍색), Y(노란색) 이용, 감산체계(색을 혼합할수록 색상이 어두워짐)
    - R-C / G-M / Y-B 는 각각 보색(Complement)관계이다.
    - CMY 컬러 모델을 사용하는 기계 : 프린터
    - CMYK 사용 이유 : CMY의 비싼 가격 때문에, 흑백을 추가하여 더 저렴하게 이용하려고

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%208.png)

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%209.png)

---

- `HSI` : 빛의 3속성(`H`ue(색상), `S`aturation(채도), `I`ntensity(명도)), 사용자가 색을 더 쉽게 지정할 수 있도록 만들었음(영상처리 유용)

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2010.png)

- H(1도~360도) : 회전각을 나타낸다. 색상에는 1도 ~ 360도 까지 있는데, 가각의 색은 서로 180도 반대편에 위치해서 어떤 색의 값에 180도를 더하면 보색을 얻을 수 있다.
- S(0%~100%) : 원의 반지름 길이이다. 중심축에 가까울수록 채도는 0에 가까우며 멀수록 1에 가깝다.
- I(0%~100%) : 원뿔의 높이이다. 아래로 갈수록 0에 가까우며, 위로 갈수록 1에 가깝다.
- (X,1,1) → 순수색상 / (X,0,1) → 흰색 / (X,0,0) → 검정색

---

- `YCbCr` : 인간의 눈이 명도에 민감 / 색상에 민감하지 않음을 이용해 만듦
    - Y : pdf에서는 휘도(책에서는 명도)
    - Cb(붉은색 정보), Cr(푸른색 정보)
    - 영상처리시 눈에 민감한 정보 Y는 그대로 유지하고, Cb와 Cr을 줄여 사용한다.
    - JPEG / MPEG에서 사용한다.
    - 💯 RGB성분에 의존적이다.(RGB정보만 있다면 YCbCr성분으로 변환 가능하다)
    - 압축해도 품질이 떨어지지 않는다.

---

- `YIQ`, `YUV` : YCbCr 컬러 모델과 거의 유사
    - Y(명도) + IQ(색상) : 북미, 우리나라 텔레비전에서 사용(NTSC)
    - Y(명도) + UV(색상) : 유럽 텔레비전에서 사용(PAL)
    - 압축해도 품질이 떨어지지 않는다.
    - 흑백 텔레비전과 호환된다 : Y성분(명도) 만으로 송출하면 되기 때문
    - RGB정보만 있다면 변환 가능하다스테레오 정합 : 두 개의 카메라를 이용한 3차원 정보 획득 기술
    
    ---
    
- 스테레오 정합 : 두 개의 카메라를 이용한 3차원 정보 획득 기술
- 조리개 : 들어오는 빛의 양을 조절(동공과 유사)
    - f2.8(빛 많이), f16(빛 조금)
- 셔터 : 카메라에서 일정 시간 동안 빛이 통과될 수 있도록 제어
    - 셔터스피드 : 셔터가 여닫히는 시간 간격
        - 빠름 : 짧은 시간동안 빛을 취득
        - 느림 : 긴 시간동안 빛을 취득

---

- 아날로그 신호 : 시간에 대하여 연속적인 신호, 자연계의 신호
- 디지털 신호 : 시간에 대하여 불연속적인 신호, 디지털과정을 거침(표본→양자→부호)

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2011.png)

- `표본화(Sampling)` : 연속된 신호 파형에서 일정한 시간 간격으로 값을 취해 불연속적인 신호로 변환하는 것
    - 표본화된 파형의 높이 값 : `표본`
    - 일정한 시간 간격 : `표본화 주기` (짧을 수록 원본과 비슷하다 BUT 데이터량이 커진다)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2012.png)
        
    - `표본화 정리(Sampling Theory)` : 원래의 아날로그 신호로 복원(정보손실 X)할 수 있는 최대 표본화 주기를 알려줌(아날로그 신호 최대 주파수의 2배 이상으로 표본화주기 잡으면 됨)
    - 주파수 = 1 / 주기
- `양자화(Quantization)` : 표본화 과정에서 얻은 표본 값을 그대로 데이터로 표현하는 것은 비효율적, 표본 값을 디지털 장치에서 표현할 수 있는 근사 값으로 변환하는 과정임
    - 양자화 비트 수 : 표본 값을 정밀하게 표현하는 데 사용하는 비트 수(2^nbit level)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2013.png)
        
- `부호화(Encoding)` : 디지털 화의 최종 단계, 양자화된 표본 값을 디지털 정보로 표현(이진수로 값을 표현)
    - 압축 부호화 : 십진수를 바로 이진수로 변환하는 것은 비효율적, 때문에 압축 부호화 사용
    - 위 그림은 압축 부호화가 아닌 일반적인 부호화를 나타냄(16LV인 것으로 보아 4bit 양자화 비트를 가짐

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2014.png)

![디지털화의 전체과정(표본화→양자화→부호화)](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2015.png)

디지털화의 전체과정(표본화→양자화→부호화)

- 신호 복원(디지털 신호 → 아날로그 신호)  : 복호화 → 아날로그화 → 평탄화(LPF)

---

- 영상신호 : 2차원 신호(가로와 세로로 차원이 2개 있음)
    - 아날로그 영상(연속색조영상) : 원래의 영상을 정확히 재현함
    - 디지털 영상 : 아날로그 영상 디지털화(표본→양자→부호) 하면 얻을 수 있음, 밝기의 불연속점으로 구성됨
- 2차원 영상신호의 표본화 : 표본화로 생성한 이산적인 점이 디지털 영상을 구성하는 최소 단위
    - 화소(Picture element), 픽셀(Pixel), 펠(Pel)
    - 표본주기 짧을 수록 화질이 좋고 데이터 양이 많아짐
- 2차원 영상신호의 양자화 : 각 화소의 밝기나 색을 정해진 몇 단계의 값으로 근사시키는 과정
    - 양자화 1bit : 2진영상
    - 양자화 2bit 이상 : 그레이레벨 영상
- 2차원 영상신호의 부호화 : 일반 데이터에 비해 영상데이터는 압도적으로 데이터양이 많기 때문에 무조건 압축 부호화를 한다.

---

- 해상도(resuloution) : 디지털 영상의 화질을 결정하는 요소
    - 공간 해상도 : 가로 축 화소 수 X 세로 축 화소 수(전체 화소 개수)
    - 밝기 해상도 : 양자화 비트수와 동일하다(얼마나 정확하게 원 영상의 명암을 표현하는지)
    - 컬러 해상도 : RGB, HSI, CMY 각각의 요소마다 공간/밝기 해상도가 존재하기 때문에 한 영상에 3개씩의 공간해상도와 밝기해상도가 존재한다.

---

- 디지털 영상의 종류 : 이진영상, 그레이레벨 영상, 컬러 영상
- `이진영상` : 화소 값이 두가지(검/흰) 밖에 없음, 값이 0 / 1 밖에 없음, 양자화 비트수 1임, 처리속도 빠름
    - 이진 영상에서 0은 무슨색인가? : 검정색 💯💯💯
    - 이진 영상에서 1은 무슨색인가? : 흰색 💯💯💯
    - 지문, 팩스, 문자 영상
- `그레이레벨 영상` : 기본적인 디지털 영상 처리 영상, 이진 영상보다 밝음, 각 화소의 밝기가 여러 단계로 나뉨(양자화 비트수에 따라 결정)
    - Gray Scale에서 0은 무슨색인가? : 검정색 💯💯💯
    - Gray Scale에서 255은 무슨색인가? : 흰색💯💯💯
    - Gray Scale에서 127은 무슨색인가? : 회색💯💯💯
    - 흑백 사진
- `컬러 영상` : 각 색을 그레이 레벨 영상처럼 독립된 형태로 처리 후, 결과를 다시 합치는 영상

---

- 디지털 영상의 구조
    - `헤더 정보부` : 파일 정보 및 보조 데이터 저장
    - `데이터부` : M x N 픽셀로 구성, 일반적으로 2차원 배열

![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2016.png)

![크기에 따른 해상도 명칭](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2017.png)

크기에 따른 해상도 명칭

- `RAW`(우리가 사용) : 헤더 정보부X, 데이터부만 존재, 사용자가 미리 영상의 크기 정보를 알 필요가 있음, 원시데이터가 있음
- `JPG(JPEG)` : 정지 영상의 압축 표준, 이미지 만드는 사람이 화질 조절 가능
- `BMP` : 비트맵 방식, 픽셀을 이차원으로 정렬, 8bit그림은 색을 나타내는데 8자리 이진수 사용, 각각의 픽셀은 숫자로 표현되는 고유의 색을 가지고 있다, 상하 반전 형태로 저장된다.(180도 회전이 아니라 좌표계가 반대를 의미한다)
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2018.png)
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2019.png)
    
    ---
    
    ---
    
    ---
    

⭐ 실습시작⭐

- Win32 API = 윈도우 운영체제가 제공하는 함수들의 묶음(ex. MessageBox()), 게임과 같은 `전체화면`을 사용하는 프로그램 개발에 좋음
- but Win32 API보다 MFC(Microsoft Foundation Class)가 더 편리하기 때문에 MFC사용 할 것임. 주로 윈도우 GUI에 기반을 두는 응용프로그램들을 개발하는 목적성을 지님
- MFC의 발전과정 알 필요 없음
- 애플리케이션 종류
    - `단일문서` : 메모장과 같이 하나의 프로그램에 하나의 창이 존재하는 구조
    - `다중문서` : Photoshop 등의 프로그램과 같이 하나의 프로그램에 여러 개의 창이 존재하는 구조
    - `Dialog Based` : 경고음과 함께 나오는 경고 메시지는 박스와 같은 구조
- 클래스 뷰 : ~~~Dlg, Doc, View등이 존재하며, 클릭하면 함수 목록 제공됨
- 리소스 뷰 : 2021108030.rc를 주로 사용하며 Dialog 추가, Menu바 추가에 사용함
- 솔루션 탐색기 : 걍 다나옴(리소스 파일, 소스 파일, 헤더 파일), 리소스 파일 클릭하면 리소스 뷰로 넘어감
- 꼭 속성에서 ‘멀티바이트 문자 집합 사용’으로 변경 해줘야 함
- 화면에 문자 출력하기 : OnDraw함수에 아래와 같이 추가

```visual-basic
pDC->TextOut(100, 100, "Hello, World!");
```

- 알림창(경고창) 띄우려면 View클래스에 이벤트 처리기를 통해 함수 생성하고 아래와 같이 추가

```visual-basic
AfxMessgaeBox("Hello, World!");
```

- MENU바에서 SUB MENU추가 후 이벤트 처리기 추가 할 때, 항상 View클래스에 함수 생성
- 우리가 사용하는 확장자 : .raw
- raw포맷 : 💯`0~255`로 구성, `8bit gray-level`(2^8), 💯`unsigned char`데이터 타입 사용
- OnOpenDocument : .Doc Class에서 재정의(override), 이 함수를 정의하기 위해 4개의 변수를 .Doc Class에 추가
    - m_InputImage(`unsigned char*`), m_width(`int`), m_height(`int`), m_size(`int`)

```cpp
	CFile File; // 파일 객체 선언

	//File.GetLength()는 전체 픽셀수를 return할 것이라고 추측
	if (File.GetLength() == 256 * 256) {
		m_height = 256;
		m_width = 256;
	}
	else if(File.GetLength() == 512 * 512) {
		m_height = 512;
		m_width = 512;
	}
	else if (File.GetLength() == 640 * 480) {
		m_height = 480;
		m_width = 640;
	}
	else {
		AfxMessageBox("Not Support Image Size");
		return 0;
	}

	m_size = m_width * m_height;
	m_InputImage = new unsigned char[m_size]; //new들어가는 것 암기

	for (int i = 0; i < m_size; i++)
		m_InputImage[i] = 255; //초기화 코드(하얀색으로)
	File.Read(m_InputImage, m_size); //암기? 까지는 안해도 될듯
	File.Close();
	// 내가 작성한 코드
```

```cpp
	int i, j;
	unsigned char R, G, B; //각 요소들은 0~255사이의 값을 지니기 때문에 unsigned char로 정의
	//기존영상출력
	for (i = 0; i < pDoc->m_height; i++) { //픽셀의 y축 길이만큼 반복
		for (j = 0; j < pDoc->m_width; j++) { //픽셀의 x축 길이만큼 반복
			R = G = B = pDoc->m_InputImage[i * pDoc->m_width + j]; //왼->오, 위->아래 순
			pDC->SetPixel(j + 5, i + 5, RGB(R, G, B)); 
			//떨어져서 출력하는게 보기 편해서, SetPixel(x축 위치값, y축 위치값, RGB함수) 암기하자
		}
	}
	//처리된영상출력
	for (i = 0; i < pDoc->m_Re_height; i++) {
		for (j = 0; j < pDoc->m_Re_width; j++) {
			R = pDoc->m_OutputImage[i * pDoc->m_Re_width + j];
			B = G = R; //흑백 영상으로 출력할 것이기 때문에 동일하게 맞춰준다.
			pDC->SetPixel(j + pDoc->m_width + 10, i + 5, RGB(R, G, B));
			//기존 영상보다 10픽셀 오른쪽에 출력시킴
		}
	}
```

- R, G, B 값이 모두 같다면 색 값은 없고 명도 값만 있는 그레이레벨 영상이 출력된다.
- OnSaveDocument함수도 .doc에서 재정의한다. 별로 안 중요해 보여서 요약정리엔 기입하지 않았다.
- 다운 샘플링 : 디지털 영상을 축소하는 가장 간단한 방법, 원 영상의 값을 일정한 좌표 단위로 버리는 것임(not 평균)
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2020.png)
    
    - Dialog를 통해 사용자로부터 값을 입력 받아야 함(`static text`, `Edit Control`)
    - Dialog 더블클릭 후 클래스를 추가해야함(C~~~Dlg)(헤더파일과 소스파일도 같이 추가 됨)
    - Dialog 클릭 후 변수도 추가해야함(m_DownSampleRate)(int)(1~32)
    - Doc에서 이번에 만든 Dialog관련 클래스를 사용할 것이기 때문에 #include “CDownSampleDlg.h”를 Doc.cpp에 추가해야함
    - 앞으로 수정된 이미지를 옆에 띄울 것이기 때문에 Doc Class에서 4개의 변수를 .Doc Class에 새롭게 추가
        - m_OutputImage(`unsigned char*`), m_Re_width(`int`), m_Re_height(`int`), m_Re_size(`int`)

```cpp
	int i, j;
	CDownSampleDlg dlg;
	if (dlg.DoModal() == IDOK) { //대화상자가 활성화 되었을 경우
		m_Re_height = m_height / dlg.m_DownSampleRate; //축소영상 높이계산
		m_Re_width = m_width / dlg.m_DownSampleRate; //축소영상 너비계산
		m_Re_size = m_Re_width * m_Re_height; //축소영상 전체 픽셀 수 계산

		m_OutputImage = new unsigned char[m_Re_size]; //new들어가는 것 암기

		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				m_OutputImage[i * m_Re_width + j]
= m_InputImage[i * m_width * dlg.m_DownSampleRate + j * dlg.m_DownSampleRate];
				//어려울 것 없음. 0123456으로 진행되는 걸 0 2 4 6 8 혹은 0 3 6 9 12 로 진행시키는 것임
			}
		}
	}
```

- Invalidate(TRUE); //화면 갱신
    - (TRUE : 화면 배경색을 포함하여 재출력, FALSE : 배경색은 그냥 두고 이외의 부분 재출력)
- pDC→ 화면 관련, pDoc→ Doc class관련
- `업 샘플링` : 단순 업 샘플링을 사용하면 품질이 너무 떨어짐, 영상을 확대해도 선명한 화질을 얻고 싶다면 보간을 해야함(BUT 여기선 일단 단순 재배열로 영상 확대 할 것임)
    - `보간` : 알려진 지점의 값 사이(중간)에 위치한 값을 알려진 값으로부터 추정하는 것
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2021.png)
        

```cpp
	int i, j;
	CUpSampleDlg dlg;
	if (dlg.DoModal() == IDOK) { //대화상자가 활성화 되었을 경우
		m_Re_height = m_height * dlg.m_UpSampleRate; //확대영상 높이 계산
		m_Re_width = m_width * dlg.m_UpSampleRate; //확대영상 너비 계산
		m_Re_size = m_Re_height * m_Re_width; //확대영상 전체 픽셀 수 계산

		m_OutputImage = new unsigned char[m_Re_size]; //new들어가는 것 암기

		for (i = 0; i < m_Re_size; i++)
			m_OutputImage[i] = 0; // 초기화(검정색(0)으로 해야 더 선명해 보임)

		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				m_OutputImage[i * m_Re_width * dlg.m_UpSampleRate + dlg.m_UpSampleRate * j]
				 = m_InputImage[i * m_width + j];
			}
		}
	}
```

- `양자화` : m_QuantBit(min : 1 ~ max : 8)

```cpp
	CQuantizationDlg dlg;
	if (dlg.DoModal() == IDOK) {
		int i, j, value, LEVEL;
		double HIGH, * TEMP;

		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		TEMP = new double[m_size];
		LEVEL = 256;
		HIGH = 256.;
		value = (int)pow(2, dlg.m_QuantBit);
		for (i = 0; i < m_size; i++) {
			for (j = 0; j < value; j++) {
				if (m_InputImage[i] >= (LEVEL / value) * j && m_InputImage[i] < (LEVEL / value) * (j + 1)) {
					TEMP[i] = (double)(HIGH / value) * j;
				}
			}
		}

		for (i = 0; i < m_size; i++)
			m_OutputImage[i] = (unsigned char)TEMP[i];
	}
```

---

- **화소 점 처리**(`포인트 처리`) : 원 화소의 값이나 위치를 바탕으로 단일 화소 값을 변경하는 기술, 다른 화소의 영향을 받지 않음
    - **Output(q) = T[Input(p)]** (p는 입력영상 화소 값, q는 출력영상 화소 값, T는 변환함수)
    - 산술연산, 논리연산, 반전, 광도 보정, 히스토그램 평활화, 명암 대비 스트레칭
- Gray-level : 0(검정)(0000 0000), 127(회색)(0111 1111), 255(흰색)(1111 1111)
- **히스토그램**(`기둥그래프`, `기둥 모양 그림`) : 관측된 데이터가 분포된 특징을 한눈에 볼 수 있도록 기둥 모양으로 나타낸 것
    - X축 : level(밝기 값), Y축 : 빈도 수(영상 내 화소 수)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2022.png)
        
    - 위 히스토그램을 보면 0부근과 255부근엔 화소가 거의 없음을 알 수 있음
    - `히스토그램 평활화` : 편중된 히스토그램을 골고루 분산시켜 영상 전체의 명암 대비를 높여줌
    - `히스토그램 명세화` : 특정 부분을 명암 대비를 높여 사용자가 원하는 히스토그램을 갖게 조작
- 화소의 밝기 값
    - 밝기의 단계 수(level) : 양자화 비트 수가 결정
    - Gray-level에서 색상X, 밝기만 O
- 명암 대비(Contrast) : 가장 밝은 값과 어두운 값의 차이, 높은 대비 일수록 더 명확하게 보임
    
    $$
    대비(Contrast) = (Imax - Imin) / (Imax + Imin)
    $$
    
- 화소 값의 **덧셈연산**(`밝기증가`) : 각 화소에 특정 상수를 더해 밝기를 증가시키는 기술
    - 처리된 화소 값이 255를 초과하면 전부 255로 대체함
- 화소 값의 **뺄셈연산**(`밝기감소`) : 각 화소에 특정 상수를 빼 밝기를 하락시키는 기술
    - 처리된 화소 값이 0보다 낮아지면(음수) 전부 0으로 대체함
- 화소 값의 **곱셈연산**(`선명도증가`) : 각 화소에 특정 상수를 곱해 밝기를 상승시키며 밝은 부분은 더 밝게, 어두운 부분은 조금 더 밝게하여 밝기차이를 증가시키는 기술
    - 255에 2를 곱했을 때 변화량과 127에 2를 곱했을 때 둘다 증가하긴 하지만 변화량은 원래 밝았던 부분이 더 큼을 이용
- 화소 값의 **나눗셈연산**(`선명도감소`) : 각 화소에 특정 상수를 나눠 밝기를 하락시키며 밝은 부분은 더 어둡게, 어두운 부분은 조금 더 어둡게하여 밝기차이를 감소시키는 기술
- 위의 4가지 산술연산의 문제점 : 결과 값이 0미만 혹은 255초과 될 수 있음
    - 해결방법 : `클래핑 기법` → 어떤 배열을 대상으로 하여 배열 내 모든 값들 중 특정한 범위 내에 속하는 것들은 그대로 살리고 범위 바깥에 속하는 것들은 범위 경계값으로 대체**(위의 4가지 기술에 적용되어 있음)**
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2023.png)
        

```cpp
	CConstantDlg dlg;
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if (m_InputImage[i] + dlg.m_Constant >= 255)
				m_OutputImage[i] = 255;
			else
				m_OutputImage[i] = (unsigned char)(m_InputImage[i] + dlg.m_Constant);
		}
	}
```

```cpp
	CConstantDlg dlg;
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if (m_InputImage[i] - dlg.m_Constant < 0)
				m_OutputImage[i] = 0;
			else
				m_OutputImage[i] = (unsigned char)(m_InputImage[i] - dlg.m_Constant);
		}
	}
```

```cpp
	CConstantDlg dlg;
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if (m_InputImage[i] * dlg.m_Constant > 255)
				m_OutputImage[i] = 255;
			else if (m_InputImage[i] * dlg.m_Constant < 0)
				m_OutputImage[i] = 0;
			else
				m_OutputImage[i] = 
				(unsigned char)(m_InputImage[i] * dlg.m_Constant);
		}
	}
```

```cpp
	CConstantDlg dlg;
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if (m_InputImage[i] / dlg.m_Constant > 255) 
				m_OutputImage[i] = 255;
			else if (m_InputImage[i] / dlg.m_Constant < 0)
				m_OutputImage[i] = 0;
			else
				m_OutputImage[i] = 
				(unsigned char)(m_InputImage[i] / dlg.m_Constant);
		}
	}
```

---

- Q : 각종 영상처리 후 붉은색 실행화면이 나오도록 변경하라
    - A : View 클래스에 정의된 OnDraw함수 내 RGB함수의 R요소를 255로 고정하면 된다.

---

- **AND연산**(`마스크(mask) 연산`) : 검검, 검흰, 흰검은 모두 검정으로 처리하고 흰흰만 흰색으로 처리함으로서, 흰색 원형 부분만 원본이 유지된다.
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2024.png)
    
- **OR연산**(`선택적-세트(selective-set) 연산`) : 검검은 검정으로, 검흰, 흰검, 흰흰은 흰색으로 처리함으로서, 테두리 부분만 원본이 유지된다.
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2025.png)
    
- **XOR연산**(`비교(compare) 연산`) : 비트가 같다 = 0, 비트가 다르다 =1
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2026.png)
    
- **NOT연산** : 비트반전, 흰색→검정, 검정→흰색
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2027.png)
    

```cpp
	CConstantDlg dlg;
	int i;

	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if ((m_InputImage[i] &|^ (unsigned char)dlg.m_Constant) >= 255)
				m_OutputImage[i] = 255;
			else if ((m_InputImage[i] &|^ (unsigned char)dlg.m_Constant) < 0)
				m_OutputImage[i] = 0;
			else
				m_OutputImage[i] = (m_InputImage[i] &|^ (unsigned char)dlg.m_Constant);
		}
	}

```

---

- `널 변환(NULL Transform)` : 입력영상 == 출력영상
    - Output(q) = Input(p)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2028.png)
        
- `반전 변환(Negative Transform)` : 각 화소 값이 대칭 값으로 변환(0→255, 255→0, 50→205)
    - Output(q) = 255 - Input(p)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2029.png)
        
- `감마 보정(Gamma Correction)` : 감마 값에 따라 밝기 조절 가능(1보다 **크면 어두워짐**, 1보다 **작으면 밝아짐,** 1이면 **널 변환**)
    - Output(q) = Input(p) * (1 / r)
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2030.png)
        
- `명암 대비 변환`
    - **명암 대비 스트레칭**(`선명도증가`) : 밝기 차이 크게 하는 것, 영상의 가장 밝은 값을 최대 밝게, 가장 어두운 값을 최대 어둡게 설정하여 대비 높이는 방법
    - **명암 대비 압축**(`선명도감소`) : 영상의 가장 어두운 값을 밝게, 가장 밝은 값을 어둡게 설정하여 대비 줄이는 방법
        
        ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2031.png)
        
- `포스터라이징(Posterizing)` : 일정 간격으로 level을 구분하여 해당 구간내에 있는 값은 하나의 값으로 통일시켜버림(경계 값 8개로 8비트 그레이 레벨 영상을 포스터라이징 처리하면, 명암 값 256개가 명암 값 8개로 변경됨)(그래프가 가장 쉽게 이해됨)
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2032.png)
    
- `이진화(Binarization)` : 경계값(T)을 기준으로 검정(0) / 흰색(1)으로만 이루어진 그림(이진 영상)으로 변환
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2033.png)
    
- `범위 강조 변환` : 특정 구간 화소의 값만 변경하여 다른 부분에 비해 더 도드라져 보이게 하는 변환(ex. 50~150사이 값들을 255로 강조)
    
    ![Untitled](Digital-mid%201e7e0777c446460e92aab2748c519544/Untitled%2034.png)
    

---

```cpp
	CQuantizationDlg dlg;
	if (dlg.DoModal() == IDOK) {
		int i, j, value, LEVEL;
		double HIGH, * TEMP;

		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		TEMP = new double[m_size];
		LEVEL = 256;
		HIGH = 256.;
		value = (int)pow(2, dlg.m_QuantBit);
		for (i = 0; i < m_size; i++) {
			for (j = 0; j < value; j++) {
				if (m_InputImage[i] >= (LEVEL / value) * j && m_InputImage[i] < (LEVEL / value) * (j + 1)) {
					TEMP[i] = (double)(HIGH / value) * j;
				}
			}
		}
		for (i = 0; i < m_size; i++)
			m_OutputImage[i] = (unsigned char)TEMP[i];
	}
```

```cpp
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	for (i = 0; i < m_size; i++)
		m_OutputImage[i] = 255 - m_InputImage[i];
```

```cpp
	CConstantDlg dlg;
	int i;
	double temp;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			temp = pow(m_InputImage[i], 1 / dlg.m_Constant);
			if (temp < 0)
				m_OutputImage[i] = 0;
			else if (temp > 255)
				m_OutputImage[i] = 255;
			else
				m_OutputImage[i] = (unsigned char)temp;
		}
	}
```

```cpp
	CConstantDlg dlg;
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	if (dlg.DoModal() == IDOK) {
		for (i = 0; i < m_size; i++) {
			if (m_InputImage[i] >= dlg.m_Constant)
				m_OutputImage[i] = 255;
			else
				m_OutputImage[i] = 0;
		}
	}
```