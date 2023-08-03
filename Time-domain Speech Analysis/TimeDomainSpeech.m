
% read sound 
[x, fs] = audioread('0011000901.wav');  %input sample for the word "dziewięć"
% normalize data
x = x / abs(max(x));
%framing
f_d = 0.020; %framing duration 20 milliseconds
frames = framing(x, fs, f_d);  % it is like  0% overlap with rectangular window


%calculate frame Energy 
[r,c] = size(frames);%number of rows and coloumn of frames
ste = 0;
for i = 1 : r
    ste(i) = sum(frames(i,:).^2);    
end
ste = ste./max(ste);   %normalize data
f_size = round(f_d * fs); %round off
ste_wave = 0;
for j = 1 : length(ste)
    l = length(ste_wave);
    ste_wave(l : l + f_size) = ste(j);
end


% plot the STE with Signal
t = [0 : 1/fs : length(x)/fs]; % time in sec
t = t(1:end - 1);
t1 = [0 : 1/fs : length(ste_wave)/fs];
t1 = t1(1:end - 1);
subplot(3,2,1)
plot(t,x'); hold on;
plot(t1,ste_wave,'r','LineWidth',2);
legend('Speech Signal','Frame Energy');
title('Speech signal and frame enegry');
subplot(3,2,2)
plot(ste,'LineWidth',2 );
title( 'short time enegry');


% Silence Removal
id = find(ste >= 0.02); %threshold value to detect the silence voice
fr_ws = frames(id,:); % frames without silence
% reconstruct signal
data_r = reshape(fr_ws',1,[]);
subplot(3,2,3);
plot(x);hold on;
plot(data_r,'g'); title('speech without silence');



% calculating Autocorelation 
for k = 1:r
t = frames(k,:);
sum1 = 0;ac = 0;
for i = 0:length(t)-1
    sum1 = 0;
    for j = 1:length(t)-i  
        s = t(j)*t(j+i);             %autocorrelation equation
        sum1 = sum1 + s;
    end
ac(i+1) = sum1;
end
temp(k) = ac(1);
stac(k) = ac(2); % taking second coeff. built in function gives normalized
% autocorrelation (it is autocorr at lag 1)
end


% short term auto corr. (stac)
stac = stac./max(stac); %normalize the data
f_size = round(f_d * fs);
stac_wave = 0;
for j = 1 : length(stac)
    l = length(stac_wave);
    stac_wave(l : l + f_size) = stac(j);
end


% plot the stac with Signal
subplot(3,2,4)
t = [0 : 1/fs : length(x)/fs]; % time in sec
t = t(1:end - 1);
t1 = [0 : 1/fs : length(stac_wave)/fs];
t1 = t1(1:end - 1);
subplot(3,2,4)
plot(t,x'); hold on;
plot(t1,stac_wave,'r','LineWidth',2);
legend('Speech Signal','Auto Corr.');
title('speech signal and Autocorrelation')

% calculating ZCR
for i = 1 : r
    xf = frames(i, :);
   ZCRf(i) = sum(abs(diff(xf > 0)));    %ZCR equation
end
ZCRr = ZCRf/length(xf);                 %ZCR rate
ZCRr = ZCRr/max(ZCRr);
f_size = round(f_d * fs);
zcr_wave = 0;
for j = 1 : length(ZCRr)
    l = length(zcr_wave);
    zcr_wave(l : l + f_size) = ZCRr(j);
end


% plot the ZCR with Signal
subplot(3,2,5)
t = [0 : 1/fs : length(x)/fs]; % time in sec
t = t(1:end - 1);
t1 = [0 : 1/fs : length(zcr_wave)/fs];
t1 = t1(1:end - 1);
plot(t,x'); hold on;
plot(t1,zcr_wave,'r','LineWidth',2);
legend('Speech Signal','zero crossing.');
title('speech signal and zero crossing')

%framing the signal speech
function [frames] = framing(x,fs,f_d)

% x:input speech signal
% fs: Sampling Frequency
% f_d: Frame duration (in sec)
% frames: returns Matrix in which each row represents a frame of specific
%         duration

f_size = round(f_d * fs);  % frame size
l_s = length(x);           % speech length
n_f = floor(l_s/f_size);   % no. of frames
temp = 0;
for i = 1 : n_f
    frames(i,:) = x(temp + 1 : temp + f_size);
    temp = temp + f_size;
end

end

