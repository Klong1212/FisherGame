# FisherGame
เกมตกปลา

โปรแกรมประกอบไปด้วย 3 หน้าจอ:
1. **StartScreen** - หน้าจอเริ่ม
2. **MainScreen** - หน้าจอเล่น
3. **BagScreen** - ช่องของ

โดย 3 หน้าจอจะลิ้งกันโดยใช้ `ScreenManager` เป็นตัวเชื่อมกัน

## StartScreen
![StartScreen](https://github.com/user-attachments/assets/d4f25b07-f078-49a6-8a67-d86ac8f18bf6)

จะเริ่มที่ StartScreen ถ้ากดปุ่ม `Start` จะเข้าสู่หน้า MainScreen

### MainScreen
![MainScreen](https://github.com/user-attachments/assets/11f0687c-4515-43a7-80c0-9ed21e35020c)

จะมีปุ่ม `Start`, `Fight`, `Bag`:
- **Start**: เกมจะเริ่มเมื่อกดปุ่ม `Start`
- **Fight**: เมื่อเกมเริ่มเราต้องกดปุ่ม `Fight` เพื่อเล่น
- **Bag**: กระเป๋า ถ้ากดจะเข้าหน้า BagScreen

#### BagScreen
![BagScreen](https://github.com/user-attachments/assets/eb4b3125-3e34-48bd-9bc7-99b9d04a3c79)

หน้าเก็บปลาและคำอธิบายปลา โดยจะไม่ขึ้นรูปปลาถ้ายังไม่ปลดล็อค

##### ตอนเล่น
เมื่อจับปลาได้:
![CatchFish1](https://github.com/user-attachments/assets/dc12b4e5-992e-415b-924e-045e7e1d7547)
![CatchFish2](https://github.com/user-attachments/assets/165a428e-3460-46e3-89f6-638df91c8ba6)