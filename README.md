# Non-Physic-Arduino-Connection

This system enables data transfer between two boards (ESP32 and Arduino UNO) within the Arduino environment without the need for physical or wireless connections, by utilizing a log file (`logs.txt`).
<br>
<br>
<img align="left" alt="Python" width="50px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"/>
<img align="left" alt="Arduino" width="50px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/arduino/arduino-original.svg"/>
<br>
<br>

## Materials

<div>
  <table>
    <tr>
      <td width="50%">
        <div align="center">
        <p> 1. Arduino UNO R3 Board</p>
        <img src="https://i.ibb.co/nR6ZPp4/71z22c-RPee-L.jpg" width="400" alt="Arduino UNO R3 Board">
        </div>
      </td>
    </tr>
  </table>
</div>
<div>
  <table>
    <tr>
      <td width="50%">
        <div align="center">
        <p> 2. ESP32 Dev Kit V1 Board</p>
        <img src="https://i.ibb.co/RDgxnNc/image-1024.jpg" width="400" alt="ESP32 Dev Kit V1 Board">
        </div>
      </td>
    </tr>
  </table>
</div>
<br>
<br>

## Usage

- This system **leverages Python** to retrieve data from the **ESP32** and logs it into a log file (`logs.txt`).
- Subsequently, the **Arduino UNO R3** reads the data from this log file and processes it accordingly.

- In the provided example code, the **ESP32 scans for available networks** and logs the data.
- The **Arduino UNO R3** then reads this data, and if it detects any network information, it **activates the integrated LED**.

- This is a **basic demonstration**, but the concept can be extended to more **complex projects**.
- Essentially, it simulates a **physical connection** between the two boards without them being physically or wirelessly connected.
- You can adapt this system to work with **any boards** and integrate it into any of your projects.
