function [designed_signal, designed_label, designed_lvec] = create_dataset(filename,signal,ann,stages,stage_label,length_interval)
designed_signal   = reshape(signal, length_interval, size(signal,1)/length_interval);
designed_label = {};
index_before = floor(ann(1)/length_interval);
label = stages(1);
for i=2:size(ann,1)
    time_to_change = ann(i);
    index_until = floor(time_to_change/length_interval);
    if index_until-index_before == 0
        error(['interval is too large around ',num2str(index_until)])
    end
    tlabels    = cell(index_until-index_before, 1);
%     display(['index_before:',num2str(index_before+1),' index_until:',num2str(index_until)])
    tlabels(:) = {label};
    if not (i ==1)
        designed_label = [designed_label; tlabels];
    else
        designed_label = tlabels;
    end
    label = stages(i);
    index_before = index_until;
end
index_until = size(signal,1)/length_interval;
tlabels    = cell(index_until-index_before, 1);
tlabels(:) = {label};
designed_label = [designed_label; tlabels].';
designed_lvec = ind2vec(cellfun(@(x) find(strcmp(stage_label,x)), designed_label),size(stage_label,1));
end