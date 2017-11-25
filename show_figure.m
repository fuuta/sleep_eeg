function [] = show_figure(signal,Fs,tm,ann,stages,stage_label)
time_interval_each_stages = cell(size(stage_label));
signal_each_stages = cell(size(stage_label));
before_index = 0;

for interval_index=1:size(ann)
    tstage = find(strcmp(stage_label,stages(interval_index)));
    time_interval_each_stages{tstage,end+1} = tm(before_index+1:ann(interval_index));
    signal_each_stages{tstage,end+1} = signal(before_index+1:ann(interval_index));
    before_index = ann(interval_index);
end
figure
cmap = colormap('jet');
% colors = {'yellow','magenta','cyan','red','green','blue','black'};
colors = cmap(1:int8(size(cmap,1)/size(stage_label,1)):size(cmap,1),:);
plots = cell(size(stage_label));
for stages=1:size(stage_label)
    for i=1:size(ann,1)+1
        if not (isempty(signal_each_stages{stages,i}))
            plot(time_interval_each_stages{stages,i},signal_each_stages{stages,i},'Color',colors(stages,:));
            hold on;grid on;
        end
    end
end

N = size(tm,1);
plot(tm(ann(ann<N)+1),signal(ann(ann<N)+1),'ro');
end