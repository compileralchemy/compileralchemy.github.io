title: Dr Murat Dogruel's Better Than April Tag Fiducial System
---
My blog post about fiducial markers [1], particularly the AprilTag papers led me to a chat with Dr. Murat Dogruel, Professor at Istanbul Sabahattin Zaim University. He presented me with a system supporting the 6 degrees of freedom he developed that might be manyfold better than AprilTag. He gave me permission to talk about the system in public for the first time.

Fiducial markers are markers recognized by systems visually, containing information that the system can use. In the case of a robot, a marker meaning pause, when read, will cause the bot to pause in its path. A QR code can act as a fiducial marker, we just encode some text. However, for robotic and industrial purposes, more performant markers are used that are fast and operate in bad conditions.

The system is really good, with documents presenting tests against AprilTag. In tests conducted,

- 6D Marker achieves almost half the error on average and a third of the maximum error compared to AprilTag. 
- April Tag does not produce stable results, especially for small scan angles. Up to 10 times or more position errors are produced by AprilTag compared to 6D Marker. - For the average and maximum angle errors, 6D Marker provides 15 times better measurement than AprilTag.
- Scan time for a 4K frame image is about 1.2ms for 6D marker and 160ms for AprilTag. 6D Marker is 130 times faster than AprilTag.

Below is a demo of a hand drill changing orientation. Notice how the system (masked by a white square) accurately reflects the drill's position.

Refs

- [1] https://lnkd.in/dvYZStr3
