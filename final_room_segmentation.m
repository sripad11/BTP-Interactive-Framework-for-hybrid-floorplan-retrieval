
function closing_doors(pys)
%I0 = imread('C:\Users\User\Desktop\wallimage_withnodoor.jpg');
I0=imread(pys)
I=im2bw(I0)
e=ones(1,180);
A=imclose(imclose(~I,e),e.');
C1=imfill(A,'holes')&~A;

I=C1
%I1 = im2bw(I0);
%I0=imread(pys)

%[m,n,~] = size(I0);
%I1 = ones(m+2,n+2);
%I1(2:end-1,2:end-1) = im2bw(I0); 


% binarize image
%I2 = bwmorph(~I1,'skel',inf);% make thin lines++++++
%imshow(I2)

%I3 = bwmorph(I2,'spur',10);         % remove spurs
%B  = bwmorph(I3,'endpoints');       % find free ends (endpoints)
%[ii,jj] = find(B);                  % find rows and columns of endpoints
%D = pdist2([ii(:) jj(:)],[ii(:) jj(:)]);    % find distances
%D(D<1e-3) = nan;                    % remove zeros
%[~,ix] = min(D);                    % find shortest distances
%for i = 1:length(ix)
%    i1 = ii(i):ii(ix(i));
%    j1 = jj(i):jj(ix(i));
%    I3(i1,j1) = 1;                  % connect door ends
%end
%I4 = imdilate(I3,ones(15));







% make lines thicker


%imshow(~I4)

%imwrite(~I4,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoor.jpg')
%imshowpair(I0,I4)




%I=im2bw(I0)
%I3 = bwmorph(~I,'skel',inf);
%I = imdilate(I3,ones(15));
%imshow(~I)
%I=~I



[L,n] = bwlabel(I);
reg=regionprops(I>0,'PixelIdxList');
B=false(size(I));
for ii = 1:n
    I = L == ii;
    

    B(reg(ii).PixelIdxList)=1;
   
    imshow(B)


    %imshow(I)
    corners = pgonCorners(I,4,360);
    
    disp(corners)
    
    array(ii,1)=corners(1)
    array(ii,2)=corners(2)
    array(ii,3)=corners(3)
    array(ii,4)=corners(4)
    array(ii,5)=corners(5)
    array(ii,6)=corners(6)
    array(ii,7)=corners(7)
    array(ii,8)=corners(8)
    hold on

 
    plot( corners(:,2),corners(:,1),'yo','MarkerFaceColor','r',...
                                'MarkerSize',12,'LineWidth',2);
    hold off
    pause(0.5)
end

for j=1:n
    bbox_loc(j,1)=array(j,1)
    bbox_loc(j,2)=array(j,2)
    bbox_loc(j,3)=array(j,3)
    bbox_loc(j,4)=array(j,4)
    bbox_loc(j,5)=array(j,5)
    bbox_loc(j,6)=array(j,6)
    bbox_loc(j,7)=array(j,7)
    bbox_loc(j,8)=array(j,8)
end
save('C:\\Users\\User\\Desktop\\cfile.mat','bbox_loc')

function corners = pgonCorners(BW,k,N)
%Method of detecting the corners in a binary image of a convex polygon with 
%a known number of vertices. Uses a linear programming approach.
%
%   corners = pgonCorners(BW,k)
%   corners = pgonCorners(BW,k,N)
%             
%IN:          
%             
%    BW: Input binary image    
%     k: Number of vertices to search for.     
%     N: Number of angular samples partitioning the unit circle (default=360).
%        Affects the resolution of the search.
%             
%OUT:         
%             
%   corners: Detected corners in counter-clockwise order as a k x 2 matrix.
   if nargin<3, N=360; end
  
    theta=linspace(0,360,N+1); theta(end)=[];
    IJ=bwboundaries(BW);
    IJ=IJ{1};
    centroid=mean(IJ);
    IJ=IJ-centroid;
    
    c=nan(size(theta));
    
    for i=1:N
        [~,c(i)]=max(IJ*[cosd(theta(i));sind(theta(i))]);
    end
    
    Ih=IJ(c,1); Jh=IJ(c,2);
    
    [H,~,~,binX,binY]=histcounts2(Ih,Jh,k);
     bin=sub2ind([k,k],binX,binY);
    
    [~,binmax] = maxk(H(:),k);
    
    [tf,loc]=ismember(bin,binmax);
    
    IJh=[Ih(tf), Jh(tf)];
    G=loc(tf);
    
    C=splitapply(@(z)mean(z,1),IJh,G);
    
    [~,perm]=sort( cart2pol(C(:,2),C(:,1)),'descend' );
    
    corners=C(perm,:)+centroid;
end
end
