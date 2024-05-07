# temporal-practice-ground
---

## 시나리오
```

API서버
- server1 : (int) -> get { +10 } 3-7초 랜덤하게 시간 걸림 
- server2 : (int) -> get { +100 } 요청즉시 50% process return fail
- server3 : (int) -> get { +4 } 요청즉시
- server4 : (int) -> get { -20 } 요청즉시
- server5 : (int) -> get {req1 + req2 + -35} 요청즉시
- server6 : (int) -> post 알리고 테스트 성공, 실패


Workflow
- server1 + server2 + server3 결과 temporal에 리턴 ( 5sec timeout ) // 실행 즉시 비동기적
- server1 -> server2 -> server3 결과 temporal에 리턴 ( 5sec timeout ) // 실행 즉시 동기적
- server1 + server2 + server4 결과 temporal에 리턴 ( 5sec timeout ) // ETA 실행시간에서 10초뒤
- server2 res + server 3 res -> server5 req -> response return // cron 서버시간 10초마다
- server6 // cron 서버시간 10분마다
- server6 // 특정이벤트 마다

Worker
- Workflows 실행
```

