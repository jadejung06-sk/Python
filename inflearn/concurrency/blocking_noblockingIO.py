'''
IO : 파일 읽거나 쓰는, 네트워크 상에서 자료 읽거나 쓰는, 데이터베이스에서 자료 읽거나 쓰는
I/O Bound : Input Output 
Blocking IO
Non-Blocking IO
Sync
Async


Blocking IO vs. Non-Blocking IO (다른 작업 수행 가능 여부 - 대기 또는 동시진행)
Blocking IO
 시스템 콜 요청 -> 커널/운영체계/ IO 작업 완료까지 응답 대기
 (IO 작업에게) 제어권 -> 커널 소유 -> 응답(response) 전 까지 대기(Block) -> 다른 작업 수행 불가(대기)
Non Blocking IO
 시스템 콜 요청 -> 커널/운영체계/ IO 작업 완료 여부 상관없이 즉시 응답 (비동기성callback함수 등)
 (IO 작업에서) 제어권 -> 유저프로세스로 제어권 전달 -> 다른 작업 수행 가능(지속적) -> "주기적으로" 시스템 콜 통해서 IO 작업 완료 여부 확인

Sync vs. Async (일 완료 확인 주체 - 능동 또는 수동)
Sync : IO 작업 완료 여부에 대한 notify는 유저프로세스(호출하는 함수) -> 커널(호출되는 함수) : 우리가 작업 완료 여부 확인
Async : IO 작업 완료 여부에 대한 notify는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수) : 운영체계가 작업 여부를 알려(callback) 주기 때문에 다른 작업들을 하고 있으면 됨

Async-NonBlocking : 유휴 시간 없이 바로 다른 작업을 수행하고 있을 수 있음
'''