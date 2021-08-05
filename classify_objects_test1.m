





function [bbox_loc,sign_objects,index1,st,furniture]=classify_objects_test1(xys)

path1='C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\fl_0sym1.tif'
path2='C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\blb_0_1.jpg'
%  clear all;
%  clc;
%  close all;
%I_initial=imread('C:\\Users\\User\\Desktop\\tkinter_codes\\floorplans\\ROBIN\\Cat1_1_3.jpg');
I_initial=imread(xys)
%I_initial = imread('room_4.png');
I=I_initial;
%imshow(I);
SE = strel('square',10);
I = imdilate(I,SE);
SE = strel('square',10);
I = imerode(I,SE);
wall_image=I;
%imshow(I)




wall = I;
I=I_initial;


wall=im2bw(wall);
%imshow(wall);
e=ones(1,180);
A=imclose(imclose(~wall,e),e.');
C=imfill(A,'holes')&A;
%imwrite(~C,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoor.jpg');
B=imfill(A,'holes')&~A;
imshow(B);
%imwrite(B,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage_withnodoors.jpg');
%[m,n] = size(figure);
%figure1 = figure(:,:,[1 1 1]);
%figure = im2bw(figure);
BW1=~B;

%BW1=im2bw(BW);
[L,num]=bwlabel(BW1);



%imwrite(wall,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage.jpg');
%skelimage=bwskel(~wall);
%imshow(skelimage);
%BW3 = bwmorph(skelimage,'skel',Inf);
%corners = detectMinEigenFeatures(BW3);
%boundaries = bwboundaries(wall);
%imshow(BW3); hold on;
%plot(corners)


I=im2bw(I);
I=imcomplement(I);
wall = imcomplement(wall);
I=I-wall;
 %imshow(I);
I=imcomplement(I);
SE = strel('square',1);
IM2 = imdilate(I,SE);


%tI am testing
IM3=imdilate(wall,SE);
%IM3=I;
IM3=imerode(IM3,SE);
IM3=imcomplement(IM3);
%imwrite(IM3,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\wallimage.jpg');

IM2 = I;
IM2 = imerode(IM2,SE);

%imwrite(IM2,'C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\fl_0sym.tif');


se1=strel('square',8);
intm1=imerode(IM2,se1);
se2=strel('square',4);
intm2=imdilate(intm1,se2);
intm3=imdilate(intm2,se2);
imwrite(intm3,path1);
I = imread(path1);
I = imcomplement(I);

J = imfill(I);
J = ~J;

imwrite(J,path2);


figure=I_initial;
[m,n] = size(figure);
figure1 = figure(:,:,[1 1 1]);
figure = im2bw(figure);
[m,n] = size(figure);
image = imread(path2);
BW = im2bw(image);
BW = imresize(BW,[m,n]);
BW = ~BW;

%Iam testing



%for 4,1,9,8
 SE = strel('square',10);
 BW = imdilate(BW,SE);
 %imshow(BW);
 
 
 BW1=imdilate(BW1,SE);
 %imshow(BW1);

 %Iam testing


  
  
  
  
  
  
  
  
  
  
 
 
% figure;imshow(BW);
st = regionprops(BW,'BoundingBox');
 shape.Inserter = vision.ShapeInserter('LineWidth',4,'BorderColor','Custom','CustomBorderColor',uint8([255 0 0]));
 
str_ele=strel('disk',1,0);
 for k = 1:length(st)
  %k=1;       
           %for k = 1:1
thisBB = st(k).BoundingBox;
%figure1 = step(shape.Inserter,figure1,bbox_loc{k});
thisBBarea=thisBB(3)*thisBB(4);
if thisBB(3)>20 &&  thisBB(4)>20 
rectangle = int32([thisBB(1),thisBB(2),thisBB(3),thisBB(4)]);


end
 if(thisBBarea >870)
bbox_loc{k}=rectangle;
 
 crop_I_new=imcrop(figure1,rectangle);
 crop_I_new_gray=rgb2gray(crop_I_new);
 crop_I=im2bw(crop_I_new_gray,0.7);
  % figure;imshow(crop_I);
signature{k}=signature_find(crop_I);
if isempty(signature{k})
   
    signature{k}=[99999,99999,99999];
end
    
  figure1 = step(shape.Inserter,figure1,bbox_loc{k});
 end
end     
signature=signature(~cellfun('isempty',signature)); 

save('signature.mat','signature');
signature=load('signature.mat');
sign_objects=load('sign_object2');
for i=1:length(signature.signature)
    for j=1:length(sign_objects.sign_object2)

diff{i,j}=abs(signature.signature{1,i}-sign_objects.sign_object2{j,1}.count);

    
    end
       
end
for(i=1:size(diff,1))
    for(j=1:size(diff,2))
        if(sign_objects.sign_object2{j,1}.count(3)>1000)
            temp1(i,j)=diff{i,j}(1)+diff{i,j}(2);
        else
            temp1(i,j)=diff{i,j}(1)+diff{i,j}(2)+diff{i,j}(3);
        end
    end
end
for(i=1:size(temp1,1))
[temp1_min(i),index1(i)]=min(temp1(i,:));  
%disp(sign_objects.sign_object2{index1(i),2});
  furniture{i,1}=sign_objects.sign_object2{index1(i),2}
 % if furniture{i,1}=={'door'}
  %    door(i)=1
  %else
   %   door(i)=0
  %end
  
  %disp(furniture{i,1})
  figure;imshow(figure1);
  %x=sprintf('C:\\Users\\User\\Desktop\\tkinter_codes\\%s.jpg',furniture{i,1})
  %imwrite(figure1,x)
bbox_loc=bbox_loc(~cellfun('isempty',bbox_loc)); 
end

disp((furniture(1)))
%n(3)=furniture{3,1}
%disp(n(3))

for(i=1:length(bbox_loc))
    %disp(furniture{i,1})
    %disp(length(bbox_loc))
    if strcmp(furniture(i),'door')
        dfile(i)=1
    else
        dfile(i)=0
    end
    
    disp(dfile(i))
end




save('C:\\Users\\User\\Desktop\\dfile.mat','dfile')
%matlab.io.saveVariablesToScript('C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\ans.mat',ans)
%save('C:\\Users\\User\\Desktop\\tkinter_codes\\obj identification\\ans.mat','ans')
save('C:\\Users\\User\\Desktop\\ans2.mat','bbox_loc')
end


%for k = 1:length(bbox_loc)
%     H= text( double(bbox_loc{k}(1)),double(bbox_loc{k}(2)),sign_objects.sign_object2{index1(k),2});
%           set(gcf,'DefaultTextColor','blue')
%end


 %for i=1:size(diff,1)
  %    for j=1:size(diff,2)
 
%         temp1(i,j)=(diff{i,j}(1));
%         temp2(i,j)=(diff{i,j}(2));
%         temp3(i,j)=(diff{i,j}(3));
 
 
 %     end
 %  [temp1_min(i),index1(i)]=min(temp1(i,:));  
 %  sign_objects=load('sign_object1');
 %  disp(sign_objects.sign_object1{index1(i),2});
 %  furniture{i,1}=sign_objects.sign_object1{index1(i),2}
 %end
 
 