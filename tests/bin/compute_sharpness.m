function [] = compute_sharpness(input_dir, output_filename)
    output_file = fopen(output_filename, 'w');

    % write header
    fprintf(output_file, 'image,sharpness\n');

    images = dir(strcat(input_dir, '/', '*.bmp'));
    for file = images'
        filename_parts = strsplit(file.name, '.');
        image = imread(strcat(input_dir, '/', file.name));
        fprintf(output_file, '%s,%d\n', filename_parts{1}, CPBD_compute(image));
    end

    fclose(output_file);
end
