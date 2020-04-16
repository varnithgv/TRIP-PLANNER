import cv2 #cv2 refers to OpenCV. Library used for image processing
import gmplot
completed=[0,0,0,0]
cost=0
KARNATAKA=[[0,440.6,426.5,145.5],[476.7,0,163.8,411.8],[425.4,163.6,0,340.6],[144.3,410.4,342.5,0]]
KERALA=[[0,53,306.4,411.9],[53,0,260.9,366.4],[306.4,260.9,0,200.8],[411.3,365.8,236.5,0]]

n=4

KARNATAKA_PLACES=["Mysore","Hubli","Hampi","Bangalore"];
KERALA_PLACES=["Alleppey","Cochin","Wayanad","Kasargod"];

KAR_FILES=["kar_m.jpg","kar_hu.jpg","kar_ha.jpg","kar_ba.jpg"];
KER_FILES=["ker_al.jpg","ker_co.jpg","ker_wa.jpg","ker_ka.jpg"];
def mincost(ary,places,city):
	i=0
	ncity=0
        global cost
	completed[city]=1
	print "%s --->" % places[(city)],
	ncity=least(ary,city)
	if(ncity==999):	
		ncity=0
		#print places[ncity]
                cost=cost+ary[city][ncity]
		return
	mincost(ary,places,ncity)

 
def least(ary,c):
	i=0
        global cost
	nc=999
	minc=999
	kmin=0
	for i in range(0,4):
		if ary[c][i]!=0 and (completed[i]==0):
			if(ary[c][i]+ary[i][c]) < minc:
			
				minc=ary[i][0]+ary[c][i]
				kmin=ary[c][i]
				nc=i
	if(minc!=999):
		cost=cost+kmin
	return nc


print " 1. Karnataka - One State Many Worlds"
print " 2. Kerala - God's own country"

ch=raw_input("\nEnter state of your choice : ")

if int(ch) == 1:

 print "\n 1. Mysore\n 2. Hubli\n 3. Hampi\n 4. Bangalore\n\n"

 sv=raw_input("Enter starting vertex\n");

 #calculate tsp with starting vertex
 mincost(KARNATAKA,KARNATAKA_PLACES,int(sv)-1) 

 #print starting vertex because in TSP we reach back to starting vertex
 print "%s\n" % KARNATAKA_PLACES[int(sv)-1]

 img = cv2.imread(KAR_FILES[int(sv)-1],cv2.IMREAD_COLOR)
 img = cv2.resize(img,(1100,650))
 cv2.imshow("Maps",img)
 
 
elif int(ch) == 2:
 print "\n 1. Alleppey\n 2. Cochin\n 3. Wayanad\n 4. Kasargod\n"
 sv=raw_input("Enter Starting vertex\n")
 mincost(KERALA,KERALA_PLACES,int(sv)-1)

 print "%s\n" % KERALA_PLACES[int(sv)-1]
 img = cv2.imread(KER_FILES[int(sv)-1])
 img = cv2.resize(img,(1100,650))
 cv2.imshow("Maps",img)
 

else:
 print "Wrong input\n"

print "Total cost is ",cost
cv2.waitKey(0)
cv2.destroyAllWindows()

