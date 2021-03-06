# [CODE] Chapter16 : 메모리를 만들어 봅시다 - 2022.03.30

<!-- TOC -->

- [[CODE] Chapter16 : 메모리를 만들어 봅시다 - 2022.03.30](#code-chapter16--%EB%A9%94%EB%AA%A8%EB%A6%AC%EB%A5%BC-%EB%A7%8C%EB%93%A4%EC%96%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4---20220330)
  - [메모리RAM](#%EB%A9%94%EB%AA%A8%EB%A6%ACram)
  - [래치LATCH](#%EB%9E%98%EC%B9%98latch)
    - [메모리를 만드는 방법](#%EB%A9%94%EB%AA%A8%EB%A6%AC%EB%A5%BC-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B0%A9%EB%B2%95)
      - [8:1 선택기](#81-%EC%84%A0%ED%83%9D%EA%B8%B0)
      - [3-8 디코더](#3-8-%EB%94%94%EC%BD%94%EB%8D%94)
    - [Random Access Memory](#random-access-memory)
    - [휘발성](#%ED%9C%98%EB%B0%9C%EC%84%B1)

<!-- /TOC -->

## `메모리(RAM)`
- 두 작업의 시점을 온전히 이어주기 위해서 정보를 보관해 두는 것

## `래치(LATCH)`
- 래치 ( 쌍 안정 멀티 바이브레이터 )는 고출력과 저출력의 두 가지 안정적인 상태를 가진 장치이다.  
  여기에는 이에 따라 피드백 레인이 포함되며 데이터는 장치에 저장 될 수 있다.  
  래치는 데이터 1비트를 저장하는 데 사용되는 메모리 장치이다.  
  이들은 플립 플롭과 동일하지만 동기식 장치가 아닙니다. FF처럼 시계의 가장자리에서 작동하지 않는다.

### `메모리를 만드는 방법`
- 1비트를 저장하는 래치를 8개를 묶으면 1바이트의 데이터를 저장 할 수 있다.  
- 래치를 응용해서 8:1 스위치와 3-8 디코더를 결합하여 만들 수 있다.

#### `8:1 선택기`
- 8개의 래치에 8비트값이 아닌 8개의 1비트 값을 관리해야 하는데
  스위치를 사용해서 각 래치들을 제어할 수 있다.
  8은 2^3 이므로 3개의 스위치만 있으면 제어가 가능하다.
  쓰기 스위치와 3개의 스위치로 하나릐 래치에 하나의 비트를 전달 할 수 있다.

#### `3-8 디코더`
- 각 래치에는 서로 다른값을 써야하는데 8개의 쓰기 입력은 같이 연결 하면 안된다.  
  즉, 한 비트 쓰기 신호가 오직 하나의 래치에만 전달될 수 있도록 만들어야 하는데  
  이때 필요한 것이 3-8 디코더 이다.
- 하나의 출력을 제외하면 모두 0의 값을 출력하는 특성이 있다.

### `Random Access Memory`
- 완전한 회로를 이루게 되면,  
  3비트의 주소는 8개의 1비트 래치들 중에 어떤 래치에 접근할 것인지 알려주는 역할을 하게 되며,  
  주소 값만 바꾸면 8개의 래치중 어디서든 값을 읽고 쓸수 있기 때문에 Random Access Memory라고 불린다.

### `휘발성`
- 임의 접근 메모리는 휘발성인데 논리 게이트에는 전자석인 릴레이들이 들어가 있다.  
  전자석에 전기가 흐르는 동안 금속 접점을 원하는 자리에 머무르게 할 수 있는데,  
  전기의 공급이 차단되면 전자석이 자성을 잃으면서 데이터들을 잃게된다.  