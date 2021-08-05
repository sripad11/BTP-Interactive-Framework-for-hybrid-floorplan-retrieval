function [count_components]=signature_find(crop_I) 
 %  figure, imshow(crop_I);
CC = bwconncomp(crop_I,4);
labeled = labelmatrix(CC); 
% RGB_label = label2rgb(labeled);
% figure, imshow(RGB_label,'InitialMagnification','fit');
u=unique(labeled);
boundarylabel=labeled(1,1);
for i=1:length(u)
    for j=1:size(labeled,1)
        for k=1:size(labeled,2)
%             if(sum(sum(labeled==i))<=1000&&(labeled(j,k)==i))
%                 labeled(j,k)=0;
%                 %disp(k);
%             end
            if (labeled(j,k)==boundarylabel)                
                labeled(j,k)=0;
            end
        end
    end
end
% RGB_label = label2rgb(labeled);
% figure, imshow(RGB_label,'InitialMagnification','fit');
u_up=unique(labeled);
for i=2:length(unique(labeled))
    count_components(i-1)=sum(sum(labeled==u_up(i)));
end
count_sort=sort(count_components,'descend');
if length(count_sort)==2
    count_sort(3)=100000000000;
end
if length(count_sort)==1
    count_sort(2)=100000000000;
    count_sort(3)=100000000000;
end
if length(count_sort)==0
    count_sort(1)=100000000000;
    count_sort(2)=100000000000;
    count_sort(3)=100000000000;
end
% if (count_sort(3))==1
%     count_sort(3)=100000000000;
% end
count_sort=count_sort(1:3);
count_components=count_sort./min(count_sort);


end