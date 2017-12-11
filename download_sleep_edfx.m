db_name = 'sleep-edfx';
db_list=physionetdb(db_name).';
for i=1:size(db_list,1)
    fname = db_list{i,1}(1:size(db_list{i,1},2)-4);
    [success,files_saved] = wfdbdownload(strcat(db_name,'/',fname));
    display([db_list{i,1}, ' success:', success, ' files_saved', files_saved])
end