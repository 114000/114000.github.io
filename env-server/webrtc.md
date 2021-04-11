# WebRTC

## 协议

<https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API/Protocols>

### 网络地址转换协议 NAT 

网络地址转换协议 Network Address Translation. 用来给你的（私网）设备映射一个公网的IP地址的协议.

内网穿透

### 交互式连接设施 ICE 

交互式连接设施 Interactive Connectivity Establishment


#### NAT会话穿越 STUN

NAT的会话穿越功能 Session Traversal Utilities for NAT


#### NAT中继穿越 TURN

NAT的中继穿越方式 Traversal Using Relays around NAT 

#### 会话描述协议 SDP

会话描述协议 Session Description Protocol 是一个描述多媒体连接内容的协议. 例如分辨率，格式，编码，加密算法等。所以在数据传输时两端都能够理解彼此的数据。本质上，这些描述内容的元数据并不是媒体流本身。

从技术上讲，SDP并不是一个真正的协议，而是一种数据格式，用于描述在设备之间共享媒体的连接。

---

## 概念

### 信令服务器 Signaling Server

## flow

### 1. 交换会话描述信息 Exchanging session descriptions

1.1 设计信令协议(字段)

``` ts
// e.g.
class SingalSessionDescription {
  type: 'video-offer' | 'video-answer',
  name: string,
  target: string,
  sdp: string
}


```

### 2. 交换 ICE 候选 Exchanging ICE candidates

两个节点需要交换ICE候选来协商他们自己具体如何连接。每一个ICE候选描述一个发送者使用的通信方法. 每个节点按照他们被发现的顺序发送候选并且保持发送直到退出，即使媒体数据流已经开始传递也要如此。


### 建立连接

### 通信

### 关闭


``` ts
// 伪代码

// peer A

// peer A's peer connection
const pcA = new RTCPeerConnection()

  // *业务功能 demo1(非必须)
  await pcA.addStream(cameraStream)

  // *业务功能 demo2(非必须)

  pcA.addTrack(stream)

  // *业务功能 demo3(非必须)
  const dc = pcA.createDataChannel('channel')
  dc.onmessage = e => console.log(e.data)
  dc.onopen = e => console.log('Connection opened!')




// peer A 是请求者
const pcAOffer = await pcA.createOffer()

// 设置 A 的本地描述, 包含peer A 的 SDP
await pcA.setLocalDescription(pcAOffer)

// 监听 ice 的变化, 重新获取 sdp
// 每次有新的节点变化时, 都会是 sdp 变化, 因为 ice 会选择最优的节点路径
// 信令服务器是自建服务, 用来交换 peer 之间的信息 http or socket
pcA.addEventListener('icecendidate', () => {
  signalingServerApi.offer(pcA.localDescription)
})

// A 接收到请求方的答复, 将对方的描述保存起来
const pcBAnswer = await signalingServerApi.onAnswer()

pc.setRemoteDescription(pcBAnswer)
// Completed!

//-----

// peer B
const pcAOffer = await signalingServerApi.onOffer()

const pcB = new RTCPeerConnection()
 

  // * 业务功能 demo3(非必须)
  let pcBDataChannel = null
  pcB.ondatachannel = (e) => {
    pcBDataChannel = e.channel 
    pcBDataChannel.onmessage = (e) => console.log(e.data)
    pcBDataChannel.onopen = (e) => console.log('Connection Opened!')
  }


await pcB.setRemoteDescription(pcAOffer)

const pcBAnswer = await pcB.createAnswer()

pcB.setLocalDescription(pcBAnswer)

// 监听 ice 的变化, 重新获取 sdp
pcA.addEventListener('icecendidate', () => {
  signalingServerApi.answer(pcB.localDescription)
})

```