f = open("udp_iptv_m3u.txt", "w")
f.write("#EXTM3U\n")
f.write("#EXTNAME:Smart TV\n")


i = 1
while i < 10:
  f.write('\n#EXTINF:'+str(i)+',Channel '+str(i)+'\n')
  f.write('rtp://@239.194.0.'+str(i)+':600'+str(i)+'\n')
  i += 1

i = 10
while i < 100:
  f.write('\n#EXTINF:'+str(i)+',Channel '+str(i)+'\n')
  f.write('rtp://@239.194.0.'+str(i)+':60'+str(i)+'\n')
  i += 1

i = 100
while i < 256:
  f.write('\n#EXTINF:'+str(i)+',Channel '+str(i)+'\n')
  f.write('rtp://@239.194.0.'+str(i)+':6'+str(i)+'\n')
  i += 1  
f.close()

#open and read the file after the appending:
#f = open("udp_iptv_m3u.txt", "r")
#print(f.read())