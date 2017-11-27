%% 


filename = 'ST7241J0-PSG.edf'
[signals,Fs,tm] = rdsamp(strcat(database_path,filename));
[ann,anntype,subtype,chan,num,comments] = rdann(strcat(database_path,filename),'hyp');
signal = signals(:,1);

stages = cellfun(@(x) flip(strsplit(x,{' ','_'})), comments,'UniformOutput',false);
stages = cellfun(@(x) char(x(3)), stages,'UniformOutput',false);
stage_label = unique(stages); % (1,2,3,4,R,W,Moving)

%%  
show_figure(signal,Fs,tm,ann,stages,stage_label)

%% 
clear all;
dataset_name = 'sleep-edfx';
database_path = strcat('database/',dataset_name,'/');
stage_label = {'1';'2';'3';'4';'R';'W';'time'};
% l_filename = cellfun(@(x) strsplit(x,{' '}), ls(strcat(database_path,'*.edf')));
l_filename = strsplit(ls(strcat(database_path,'*.edf')),{'\t','\n'}).';

is_first = 1;

for k=1:length(l_filename)
    filename = l_filename{k,1};
    try
        display([filename]);
        [signals,Fs,tm] = rdsamp(filename);
        [ann,anntype,subtype,chan,num,comments] = rdann(filename,'hyp');
        info = wfdbdesc(strcat(dataset_name,filename));
        save(strcat(filename,'.mat'),'signals','Fs','tm','ann','anntype','subtype','chan','num','comments')
        signal = signals(:,1);

        stages = cellfun(@(x) flip(strsplit(x,{' ','_'})), comments,'UniformOutput',false);
        stages = cellfun(@(x) char(x(3)), stages,'UniformOutput',false);

        [devsig,devlab, devlab_vec] = create_dataset(filename,signal,ann,stages,stage_label,1000);
        if is_first
            input_data = devsig;
            label_data = devlab;
            output_data = devlab_vec;
            is_first = 0;
        else
            input_data = [input_data,devsig];
            label_data = [label_data,devlab];
            output_data = [output_data,devlab_vec];
        end
    catch 
        warning(['cant load data',filename]);
    end
end



