Python Task 1
________________________

1 # Car-Matrix-Generation-

import pandas as pd

def generate_car_matrix(dataset):
    df = pd.read_csv(dataset)
    
    result_df = df.pivot(index='id_1', columns='id_2', values='car')
    
    result_df = result_df.fillna(0)
    
    result_df.values[[range(len(result_df))]*2] = 0
    
    return result_df

# Example usage
dataset_path = 'dataset-1.csv'
result_dataframe = generate_car_matrix(dataset_path)

# Print the resulting DataFrame
print(result_dataframe)
--------------------------------
Question 2: Car Type Count Calculation


import pandas as pd

def get_type_count(dataset):
    df = dataset.copy()

    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    type_count = df['car_type'].value_counts().to_dict()

    type_count = dict(sorted(type_count.items()))

    return type_count

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_type_count = get_type_count(df)

# Print the resulting type count dictionary
print(result_type_count)

----------------------------------
Question 3: Bus Count Index Retrieval

import pandas as pd

def get_bus_indexes(dataset):
    mean_bus_value = dataset['bus'].mean()

    bus_indexes = dataset[dataset['bus'] > 2 * mean_bus_value].index.tolist()

    bus_indexes.sort()

    return bus_indexes

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_bus_indexes = get_bus_indexes(df)

# Print the resulting bus indexes
print(result_bus_indexes)

-------------------------------------
Question 4: Route Filtering


import pandas as pd

def filter_routes(dataset):
    route_means = dataset.groupby('route')['truck'].mean()

    filtered_routes = route_means[route_means > 7].index.tolist()

    filtered_routes.sort()

    return filtered_routes

# Example usage
dataset_path = 'dataset-1.csv'
df = pd.read_csv(dataset_path)
result_filtered_routes = filter_routes(df)

# Print the resulting list of filtered routes
print(result_filtered_routes)

----------------------------------
Question 5: Matrix Value Modification


import pandas as pd

def multiply_matrix(input_matrix):
    modified_matrix = input_matrix.copy()

    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage
result_dataframe = generate_car_matrix('dataset-1.csv')
result_modified_matrix = multiply_matrix(result_dataframe)

# Print the resulting modified DataFrame
print(result_modified_matrix)

--------------------------------
Question 6: Time Check


import pandas as pd

def check_time_completeness(dataset):
    dataset['start_datetime'] = pd.to_datetime(dataset['startDay'] + ' ' + dataset['startTime'])
    dataset['end_datetime'] = pd.to_datetime(dataset['endDay'] + ' ' + dataset['endTime'])

    dataset['day_of_week'] = dataset['start_datetime'].dt.day_name()
    dataset['start_time'] = dataset['start_datetime'].dt.time
    dataset['end_time'] = dataset['end_datetime'].dt.time

    expected_start_time = pd.Timestamp('1900-01-01 00:00:00').time()
    expected_end_time = pd.Timestamp('1900-01-01 23:59:59').time()

    incorrect_timestamps = (
        (dataset['start_time'] != expected_start_time) |
        (dataset['end_time'] != expected_end_time) |
        ~dataset['day_of_week'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    )

    boolean_series = incorrect_timestamps.groupby(['id', 'id_2']).any()

    return boolean_series

# Example usage
dataset_path = 'dataset-2.csv'
df = pd.read_csv(dataset_path)
result_boolean_series = check_time_completeness(df)

# Print the resulting boolean series
print(result_boolean_series)
