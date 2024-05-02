# temporal-practice-ground
---

## 시나리오
```

API서버
- server1 : (int) -> { +10 } 3-7초 랜덤하게 시간 걸림 
- server2 : (int) -> { +100 } 요청즉시 50% process return fail
- server3 : (int) -> { +4 } 요청즉시
- server4 : (int) -> { -20 } 요청즉시


Workflow
- server1 + server2 + server3 결과 temporal에 리턴 ( 5sec timeout )
- server1 + server2 + server4 결과 temporal에 리턴 ( 5sec timeout )

Worker
- Workflows 실행
```

