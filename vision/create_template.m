clear all;
close all;


num = '062';
material = 'metal';
numstart = 31;

im = imread(['training/' material '/img' num '.jpg']);

figure;
imshow(im);

[x,y] = ginput(2);



cMM = round(x);
rMM = round(y);

m = randi([cMM(1) cMM(2)-100], 10, 1);
n = randi([rMM(1) rMM(2)-100], 10, 1);
%m = [392 502 300 606 552 ];
%n = [74 293 436 595 383 ];

for i = 1:length(m)

imSmall = im(n(i):n(i)+99,m(i):m(i)+99,:);
imwrite(imSmall,sprintf('training/%s_Template/patch%03d.jpg', material, numstart + i - 1) );

end
% figure;
% image(im)
% 
% figure;
% image(imSmall)