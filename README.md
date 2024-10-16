## About The Project

Sunscope is a user-friendly platform designed to simplify solar energy adoption for households. By leveraging satellite imagery from Google Earth or Google Maps, users can easily upload images of their rooftops. Using our trained YOLO v11 model, Sunscope automatically annotates the rooftop and calculates the available surface area. Based on this, the platform estimates the number of solar panels that can be installed. Additionally, users can input their monthly electricity bills to receive personalized insights on potential annual savings from solar energy. Sunscope aims to reduce electricity costs, promote sustainability, and enhance awareness about the benefits of solar power



![home](https://github.com/user-attachments/assets/766a6d33-5f89-4708-b922-9fa7ea9a3288)


# Built With
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

<!-- GETTING STARTED -->
## Getting Started

In this section you should provide instructions on how to use this repository to recreate your project locally.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Adityapratapsingh28/Sunscope
   ```

### Dependencies

Here, list all libraries, packages and other dependencies that need to be installed to run your project. Include library versions and how they should be installed if a special requirement is needed.

> Make sure you make requirements.txt having all the dependencies required to run the code

For example, this is how you would list them:
* Installing all dependencies
  ```sh
  pip install -r requirements.txt
  ```
* Example of requirements.txt
  ```sh
  ultralytics
  flask
  opencv-python-headless
  ```
## Video tutorial to run locally









https://github.com/user-attachments/assets/401619b9-b1db-4652-bd98-77b30be6f6b4





<!-- USAGE EXAMPLES -->
## Problem Statement

Many households face high electricity bills, especially during summer, due to limited use of solar energy. Despite the benefits of solar power, such as reducing electricity costs and supporting sustainability, users often struggle with the complexity of determining how many solar panels can fit on their roof and how much they could save. A lack of knowledge and awareness about solar energy adoption further hinders their ability to make informed decisions.





<!-- ROADMAP -->
## Key Features 🤖
- Simplified and user frirendly UI

   - We have provided a simple page to upload the rooftop image and to enter the monhtly electricity bill
 


     
![calculate](https://github.com/user-attachments/assets/60aa54f4-1951-41e1-b49e-9cc342c2db5c)


- Accurate Detection & display of savings

   - When the user will enter the rooftop & his electricity bill , our website will show the total rooftop area, estimated solar potential, number of solar panels and estimated annual savings
 
     
 

![result](https://github.com/user-attachments/assets/24790ab8-54b1-4173-bb2b-ffb72b2a5526)

 
- Sustainability

   - Promotes long-term sustainability by supporting the adoption of renewable solar energy solutions.



![sustainability](https://github.com/user-attachments/assets/52679962-18bb-42e1-a35b-36fba4214be9)



- Cost Savings

  - Provides personalized estimates of annual savings based on your electricity bill and rooftop solar potential
 

![cost savings](https://github.com/user-attachments/assets/f8301c97-c6be-4af8-a146-46554d237691)



- Reduced Carbon Emissions
   - Solar energy helps cut down on greenhouse gas emissions by replacing fossil fuel-based electricity with clean, renewable power
 
     
![positive env impact](https://github.com/user-attachments/assets/d9a65cf4-09c9-4c4b-bfe7-7a7ed6172530)

- Enhanced Model Training:

  - Our YOLO v11 model is trained on a large amount of dataset in order to predict the correct rooftop annotation
 



![Screenshot 2024-10-16 065617](https://github.com/user-attachments/assets/03dc7d25-a7bf-4676-9ac9-e5b5fde34939)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- Authors -->
## Authors

Nilesh Kanti - [Linkedin](https://www.linkedin.com/in/nileshkanti/) 

Aditya Pratap Singh - [Linkedin](https://www.linkedin.com/in/aditya-singhpratapsingh8a4a62287?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
