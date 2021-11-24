# Output

- Installs firefox, chromium
- One demo program (main.py) to pass the arguments
- `.env` -> environment variable to set arguments to share inside Docker/ Python in Docker
- 



```
──> docker-compose  up --build                                                                                                                                                                                     ──(Wed,Nov24)─┘
Sending build context to Docker daemon     534B
Step 1/5 : FROM python:3.7-alpine
 ---> f0c1a69798c7
Step 2/5 : WORKDIR /CODE
 ---> Using cache
 ---> 731d508e355b
Step 3/5 : RUN apk add --no-cache gcc musl-dev linux-headers firefox chromium
 ---> Running in 3ebdc913c0fd
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz
(1/127) Installing libxau (1.0.9-r0)
(2/127) Installing libmd (1.0.3-r0)
(3/127) Installing libbsd (0.11.3-r0)
(4/127) Installing libxdmcp (1.1.3-r0)
(5/127) Installing libxcb (1.14-r2)
(6/127) Installing libx11 (1.7.2-r0)
(7/127) Installing libxext (1.3.4-r0)
(8/127) Installing libice (1.0.10-r0)
(9/127) Installing libsm (1.2.3-r0)
(10/127) Installing libxt (1.2.1-r0)
(11/127) Installing libxmu (1.1.3-r0)
(12/127) Installing xset (1.2.4-r0)
(13/127) Installing xprop (1.2.5-r0)
(14/127) Installing xdg-utils (1.1.3-r0)
(15/127) Installing eudev-libs (3.2.10-r0)
(16/127) Installing brotli-libs (1.0.9-r5)
(17/127) Installing libpng (1.6.37-r1)
(18/127) Installing freetype (2.10.4-r1)
(19/127) Installing fontconfig (2.13.1-r4)
(20/127) Installing libfontenc (1.1.4-r0)
(21/127) Installing mkfontscale (1.2.1-r1)
(22/127) Installing ttf-opensans (1.10-r1)
Executing ttf-opensans-1.10-r1.post-install
(23/127) Installing libgcc (10.3.1_git20210424-r2)
(24/127) Installing libogg (1.3.5-r0)
(25/127) Installing libstdc++ (10.3.1_git20210424-r2)
(26/127) Installing flac (1.3.3-r0)
(27/127) Installing libxcomposite (0.4.5-r0)
(28/127) Installing libxdamage (1.1.5-r1)
(29/127) Installing libxfixes (6.0.0-r0)
(30/127) Installing libxrender (0.9.10-r3)
(31/127) Installing libxrandr (1.5.2-r1)
(32/127) Installing alsa-lib (1.2.5-r2)
(33/127) Installing libblkid (2.37.2-r0)
(34/127) Installing libmount (2.37.2-r0)
(35/127) Installing pcre (8.44-r0)
(36/127) Installing glib (2.68.3-r0)
(37/127) Installing atk (2.36.0-r0)
(38/127) Installing libxi (1.7.10-r0)
(39/127) Installing libxtst (1.2.3-r3)
(40/127) Installing dbus-libs (1.12.20-r2)
(41/127) Installing at-spi2-core (2.40.0-r0)
(42/127) Installing at-spi2-atk (2.38.0-r0)
(43/127) Installing libatomic (10.3.1_git20210424-r2)
(44/127) Installing sdl2 (2.0.14-r1)
(45/127) Installing aom-libs (1.0.0-r3)
(46/127) Installing fribidi (1.0.10-r0)
(47/127) Installing graphite2 (1.3.14-r0)
(48/127) Installing harfbuzz (2.8.1-r0)
(49/127) Installing libass (0.15.1-r0)
(50/127) Installing libdav1d (0.9.0-r0)
(51/127) Installing gmp (6.2.1-r0)
(52/127) Installing nettle (3.7.3-r0)
(53/127) Installing p11-kit (0.23.22-r0)
(54/127) Installing libtasn1 (4.17.0-r0)
(55/127) Installing libunistring (0.9.10-r1)
(56/127) Installing gnutls (3.7.1-r0)
(57/127) Installing lame (3.100-r0)
(58/127) Installing opus (1.3.1-r1)
(59/127) Installing libgomp (10.3.1_git20210424-r2)
(60/127) Installing soxr (0.1.3-r2)
(61/127) Installing libsrt (1.4.2-r0)
(62/127) Installing libssh (0.9.6-r0)
(63/127) Installing libtheora (1.1.1-r16)
(64/127) Installing libjpeg-turbo (2.1.0-r0)
(65/127) Installing v4l-utils-libs (1.20.0-r0)
(66/127) Installing libpciaccess (0.16-r0)
(67/127) Installing libdrm (2.4.106-r0)
(68/127) Installing wayland-libs-client (1.19.0-r0)
(69/127) Installing libva (2.11.0-r0)
(70/127) Installing libvdpau (1.4-r0)
(71/127) Installing vidstab (1.1.0-r1)
(72/127) Installing libvorbis (1.3.7-r0)
(73/127) Installing libvpx (1.10.0-r0)
(74/127) Installing vulkan-loader (1.2.170-r1)
(75/127) Installing libwebp (1.2.0-r2)
(76/127) Installing x264-libs (20210211-r0)
(77/127) Installing x265-libs (3.4-r0)
(78/127) Installing xvidcore (1.3.7-r1)
(79/127) Installing ffmpeg-libs (4.4.1-r0)
(80/127) Installing pixman (0.40.0-r2)
(81/127) Installing cairo (1.16.0-r3)
(82/127) Installing avahi-libs (0.8-r5)
(83/127) Installing cups-libs (2.3.3-r2)
(84/127) Installing libevent (2.1.12-r2)
(85/127) Installing mesa (21.1.2-r0)
(86/127) Installing wayland-libs-server (1.19.0-r0)
(87/127) Installing mesa-gbm (21.1.2-r0)
(88/127) Installing lcms2 (2.12-r1)
(89/127) Installing nspr (4.31-r0)
(90/127) Installing nss (3.66-r0)
(91/127) Installing libxft (2.3.3-r0)
(92/127) Installing pango (1.48.5-r0)
(93/127) Installing re2 (2021.06.01-r0)
(94/127) Installing snappy (1.1.8-r2)
(95/127) Installing pkgconf (1.7.4-r0)
(96/127) Installing xkeyboard-config (2.33-r0)
(97/127) Installing libxml2 (2.9.12-r1)
(98/127) Installing libxkbcommon (1.2.1-r0)
(99/127) Installing libxshmfence (1.3-r1)
(100/127) Installing libgpg-error (1.42-r0)
(101/127) Installing libgcrypt (1.9.4-r0)
(102/127) Installing libxslt (1.1.34-r1)
(103/127) Installing chromium (93.0.4577.82-r0)
(104/127) Installing libxcursor (1.2.0-r0)
(105/127) Installing cairo-gobject (1.16.0-r3)
(106/127) Installing dbus-glib (0.112-r0)
(107/127) Installing shared-mime-info (2.1-r0)
(108/127) Installing hicolor-icon-theme (0.17-r1)
(109/127) Installing zstd-libs (1.4.9-r1)
(110/127) Installing tiff (4.2.0-r1)
(111/127) Installing gdk-pixbuf (2.42.6-r0)
(112/127) Installing gtk-update-icon-cache (2.24.33-r0)
(113/127) Installing libxinerama (1.1.4-r1)
(114/127) Installing libepoxy (1.5.8-r0)
(115/127) Installing wayland-libs-cursor (1.19.0-r0)
(116/127) Installing wayland-libs-egl (1.19.0-r0)
(117/127) Installing gtk+3.0 (3.24.28-r0)
Executing gtk+3.0-3.24.28-r0.post-install
(118/127) Installing icu-libs (67.1-r2)
(119/127) Installing firefox (89.0.1-r0)
(120/127) Installing binutils (2.35.2-r2)
(121/127) Installing libgphobos (10.3.1_git20210424-r2)
(122/127) Installing isl22 (0.22-r0)
(123/127) Installing mpfr4 (4.1.0-r0)
(124/127) Installing mpc1 (1.2.1-r0)
(125/127) Installing gcc (10.3.1_git20210424-r2)
(126/127) Installing linux-headers (5.10.41-r0)
(127/127) Installing musl-dev (1.2.2-r3)
Executing busybox-1.33.1-r6.trigger
Executing fontconfig-2.13.1-r4.trigger
Executing mkfontscale-1.2.1-r1.trigger
Executing glib-2.68.3-r0.trigger
Executing shared-mime-info-2.1-r0.trigger
Executing gdk-pixbuf-2.42.6-r0.trigger
Executing gtk-update-icon-cache-2.24.33-r0.trigger
OK: 654 MiB in 162 packages
 ---> eb2ffdfaa2b1
Step 4/5 : COPY . .
 ---> 34a19f4f8f74
Step 5/5 : CMD ["python", "main.py"]
 ---> Running in d2052a2c1808
 ---> d693c60f6e4f
Successfully built d693c60f6e4f
Successfully tagged composetest_main:latest
[+] Running 1/0
 ⠿ Container composetest-main-1  Recreated                                                                                                                                                                                                0.1s
Attaching to composetest-main-1
composetest-main-1  | Number of arguments: 1 arguments.
composetest-main-1  | Argument List: ['main.py'] 123
composetest-main-1 exited with code 0

```
