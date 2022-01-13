## 주차장 관리 프로그램(Side Project)
![image](https://user-images.githubusercontent.com/62638100/149361907-482ee1a2-875a-4072-b758-244e21e5321a.png)
![current_parking_lot](https://user-images.githubusercontent.com/62638100/149156534-7cd7ed05-df8d-4acb-abcc-138c8f1064a3.jpg)

#### ParkingLotMonitoringServer
주차장 상태 파악을 위해서 실시간 영상을 이용한다면 더욱 좋겠지만, 주차장 영상으로 대체하였습니다. ([영상출처](https://www.computervision.zone/courses/parking-space-counter/))
해당 영상을 1초 마다 읽고 분석하여 주차장의 차량 여부와 현재 이미지를 저장합니다.

#### ParkingLotServer
사용자에게 주차장 상태를 제공하는 웹서버입니다. ParkingLotMonitoringServer로 부터 저장된 정보를 불러와 사용자에게 제공합니다.
또한 주차장 자리를 예약하는 기능 또한 개발 예정입니다.
