# Digital-final(Code)

# 🧑‍💻 6장 - 화소영역처리

- Image2DMem : 화소 영역 처리 프로그램을 간단히 하려고 **1차원 배열을 2차원 배열로 할당**하는 함수

```cpp
double** CImageProcessing2021108030Doc::Image2DMem(int height, int width)
{
	double** temp;
	int i, j;
	temp = new double* [height];
	for (i = 0; i < height; i++) {
		temp[i] = new double[width];
	}
	for (i = 0; i < height; i++) {
		for (j = 0; j < width; j++) {
			temp[i][j] = 0.0;
		}
	}

	return temp;
}
```

- OnMaskProcess : 화소 영역을 처리하는 함수

```cpp
double** CImageProcessing2021108030Doc::OnMaskProcess3x3(unsigned char *Target, double Mask[3][3])
{
	int i, j, n, m;
	double** tempInputImage, ** tempOutputImage, S = 0.0;
	tempInputImage = Image2DMem(m_height + 2, m_width + 2);
	tempOutputImage = Image2DMem(m_height, m_width);

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			tempInputImage[i + 1][j + 1] =
				(double)Target[i * m_width + j];
		}
	}
	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			for (n = 0; n < 3; n++) {
				for (m = 0; m < 3; m++) {
					S += Mask[n][m] * tempInputImage[i + n][j + m];
				}
			}
			tempOutputImage[i][j] = S;
			S = 0.0;
		}
	}

	return tempOutputImage;
}
```

- OnEmbossing : 엠보싱 함수

```cpp
void CImageProcessing2021108030Doc::OnEmbossing()
{
	int i, j;
	double EmboMask[3][3] = {{-1., 0., 0.}, {0., 0., 0.}, {0., 0., 1.}};
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess3x3(m_InputImage, EmboMask);
	//시험 : &를 붙여 작동되게 바꿔보아라!
	//m_tempImage = OnMaskProcess3x3(&m_InputImage[0], &EmboMask[0]);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
			= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

- OnBlurr : 블러링 함수

```cpp
void CImageProcessing2021108030Doc::OnBlurr()
{
	int i, j;
	double BlurrMask[5][5] = {{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.},
				{1. / 25., 1. / 25., 1. / 25., 1. / 25., 1. / 25.} };
	/*double BlurrMask[3][3] = { {1. / 9., 1. / 9., 1. / 9.},
	{1. / 9., 1. / 9., 1. / 9.}, {1. / 9., 1. / 9., 1. / 9.}};*/
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	//m_tempImage = OnMaskProcess3x3(m_InputImage, BlurrMask);
	m_tempImage = OnMaskProcess5x5(m_InputImage, BlurrMask);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

- OnGaussianFilter : 스무딩 처리 중 가우시안 필터 사용 함수

```cpp
void CImageProcessing2021108030Doc::OnGaussianFilter()
{
	int i, j;
	double GaussianMask[3][3] = { {1./16., 1./8., 1./16.},
	{1. / 8., 1. / 4., 1. / 8.}, {1. / 16., 1. / 8., 1. / 16.}};
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess3x3(m_InputImage, GaussianMask);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

- OnSharpening : 샤프닝 함수

```cpp
void CImageProcessing2021108030Doc::OnSharpening()
{
	int i, j;
	double SharpeningMask[3][3] = { {-1., -1., -1.},
	{-1., 9., -1.}, {-1., -1., -1.}};
	/*double SharpeningMask[3][3] = {{0., -1., 0.},
	{-1., 5., -1.}, {0., -1., 0.} };*/
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess3x3(m_InputImage, SharpeningMask);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

- OnHpfSharp : 고주파 필터 샤프닝 함수

```cpp
void CImageProcessing2021108030Doc::OnHpfSharp()
{
	int i, j;
	double HpfSharpMask[3][3] = { {-1. / 9., -1. / 9., -1. / 9.},
	{-1. / 9., 8. / 9., -1. / 9.}, {-1. / 9., -1. / 9., -1. / 9.} };
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess3x3(m_InputImage, HpfSharpMask);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

---

# 🧑‍💻 7장 - 에지 검출

- OnDiffOperator : 이동과 차분(1 : 수평, 2 : 수직)

```cpp
void CImageProcessing2021108030Doc::OnDiffOperator()
{
	int i, j;
	double DiffHorMask1[3][3] = { {0., -1., 0.},{0., 1., 0.},{0., 0., 0.} }; //수평
	double DiffHorMask2[3][3] = { {0., 0., 0.},{-1., 1., 0.},{0., 0., 0.} }; //수직
	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = OnMaskProcess3x3(m_InputImage, DiffHorMask1);

	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (m_tempImage[i][j] > 255.)
				m_tempImage[i][j] = 255.;
			if (m_tempImage[i][j] < 0.)
				m_tempImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)m_tempImage[i][j];
		}
	}
}
```

- DoubleABS : 절대값 변환 함수

```cpp
double CImageProcessing2021108030Doc::DoubleABS(double X)
{
	if (X >= 0) {
		return X;
	}
	else {
		return -X;
	}
}
```

- OnHomogenOperator : 유사 연산자 기법

```cpp
void CImageProcessing2021108030Doc::OnHomogenOperator()
{
	int i, j, n, m;
	double max, ** tempOutputImage;

	m_Re_width = m_width;
	m_Re_height = m_height;
	m_Re_size = m_Re_width * m_Re_height;
	m_OutputImage = new unsigned char[m_Re_size];
	
	m_tempImage = Image2DMem(m_height + 2, m_width + 2);
	tempOutputImage = Image2DMem(m_Re_height, m_Re_width);

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_tempImage[i + 1][j + 1] = (double)m_InputImage[i * m_width + j];
		}
	}
	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			max = 0.0;
			for (n = 0; n < 3; n++) {
				for (m = 0; m < 3; m++) {
					if (DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]) >= max)
						max = DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]);
				}
			}
			tempOutputImage[i][j] = max;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			if (tempOutputImage[i][j] > 255.)
				tempOutputImage[i][j] = 255.;
			if (tempOutputImage[i][j] < 0.)
				tempOutputImage[i][j] = 0.;
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j]
				= (unsigned char)tempOutputImage[i][j];
		}
	}
}
```

- OnHomogenOperatorThreshold : 유사 연산자 기법 + 임계값 추가

```cpp
void CImageProcessing2021108030Doc::OnHomogenOperatorThreshold()
{
	int i, j, n, m;
	double max, ** tempOutputImage;
	CHomogenOperatorThresholdDlg dlg;
	if (dlg.DoModal() == IDOK) { //dialog에서 OK가 눌렸을 경우 실행
		//SWAP(입력받는 2개의 변수 중 무엇이 더 값이 클지 모르기 때문에 val1 <= val2를 유지하기 위한 코드)
		if (dlg.val1 > dlg.val2) {
			double temp = dlg.val1;
			dlg.val1 = dlg.val2;
			dlg.val2 = temp;
		}
		m_Re_width = m_width;
		m_Re_height = m_height;
		m_Re_size = m_Re_width * m_Re_height;
		m_OutputImage = new unsigned char[m_Re_size];

		m_tempImage = Image2DMem(m_height + 2, m_width + 2);
		tempOutputImage = Image2DMem(m_Re_height, m_Re_width);

		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				m_tempImage[i + 1][j + 1] = (double)m_InputImage[i * m_width + j];
			}
		}
		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				max = 0.0;
				for (n = 0; n < 3; n++) {
					for (m = 0; m < 3; m++) {
						if (DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]) >= max)
							max = DoubleABS(m_tempImage[i + 1][j + 1] - m_tempImage[i + n][j + m]);
					}
				}
				//다중 임계값으로 처리하기 위한 코드(단, val1 <= val2)
				//두 경계 값 보다 큰 값이 올 경우 255로 초기화 
				//두 경계 값 사이의 값이 올 경우 가장 큰 경계값으로 초기화
				//두 경계 값 보다 작은 값이 올 경우 0으로 초기화
				if (dlg.val2 < max)
					max = 255.;
				else if (dlg.val1 <= max && max <= dlg.val2)
					max = dlg.val2;
				else if (dlg.val1 > max)
					max = 0.;
				tempOutputImage[i][j] = max;
			}
		}
		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				if (tempOutputImage[i][j] > 255.)
					tempOutputImage[i][j] = 255.;
				if (tempOutputImage[i][j] < 0.)
					tempOutputImage[i][j] = 0.;
			}
		}
		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				m_OutputImage[i * m_Re_width + j]
					= (unsigned char)tempOutputImage[i][j];
			}
		}
	}
}
```

---

# 🧑‍💻 8장 - 기하학적 변화

- OnNearest : 가장 인접한 이웃화소 보간법

```cpp
void CImageProcessing2021108030Doc::OnNearest()
{
	int i, j;
	int ZoomRate = 2;
	double** tempArray;

	m_Re_height = int(ZoomRate * m_height);
	m_Re_width = int(ZoomRate * m_width);
	m_Re_size = m_Re_height * m_Re_width;
	m_tempImage = Image2DMem(m_height, m_width);
	tempArray = Image2DMem(m_Re_height, m_Re_width);
	m_OutputImage = new unsigned char[m_Re_size];

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			tempArray[i][j] = m_tempImage[i / ZoomRate][j / ZoomRate];
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			m_OutputImage[i * m_Re_width + j] = (unsigned char)tempArray[i][j];
		}
	}
}
```

- OnBilinear : 양선형 보간법

```cpp
void CImageProcessing2021108030Doc::OnBilinear()
{
	int i, j, point, i_H, i_W;
	unsigned char newValue;
	double ZoomRate = 2.0, r_H, r_W, s_H, s_W;
	double C1, C2, C3, C4;

	m_Re_height = (int)(m_height * ZoomRate);
	m_Re_width = (int)(m_width * ZoomRate);
	m_Re_size = m_Re_height * m_Re_width;
	m_tempImage = Image2DMem(m_height, m_width);
	m_OutputImage = new unsigned char[m_Re_size];

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
		}
	}
	for (i = 0; i < m_Re_height; i++) {
		for (j = 0; j < m_Re_width; j++) {
			r_H = i / ZoomRate;
			r_W = j / ZoomRate;
			i_H = (int)floor(r_H);
			i_W = (int)floor(r_W);
			s_H = r_H - i_H;
			s_W = r_W - i_W;

			if (i_H < 0 || i_H >= (m_height - 1) || i_W < 0 || i_W >= (m_width - 1)) {
				point = i * m_Re_width + j;
				m_OutputImage[point] = 255;
			}
			else {
				C1 = (double)m_tempImage[i_H][i_W];
				C2 = (double)m_tempImage[i_H][i_W + 1];
				C3 = (double)m_tempImage[i_H + 1][i_W + 1];
				C4 = (double)m_tempImage[i_H + 1][i_W];

				newValue = (unsigned char)(C1 * (1 - s_H) * (1 - s_W) + C2 * s_W
					* (1 - s_H) + C3 * s_W * s_H + C4 * (1 - s_W) * s_H);
				point = i * m_Re_width + j;
				m_OutputImage[point] = newValue;
			}
		}
	}
}
```

- BubbleSort & Swap

```cpp
void CImageProcessing2021108030Doc::OnBubbleSort(double* A, int MAX)
{
	int i, j;
	for (i = 0; i < MAX; i++) {
		for (j = 0; j < MAX; j++) {
			if (A[j] > A[j + 1])
				OnSwap(&A[j], &A[j + 1]);
		}
	}
}

void CImageProcessing2021108030Doc::OnSwap(double* a, double* b)
{
	double temp = *a;
	*a = *b;
	*b = temp;
}
```

- OnMedianSub : 미디언 서브 샘플링

```cpp
void CImageProcessing2021108030Doc::OnMedianSub()
{
	int i, j, n, m, M = 4, index = 0; // M = 서브 샘플링 비율
	double* Mask, Value;
	
	Mask = new double[M * M];

	m_Re_height = m_height / M;
	m_Re_width = m_width / M;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = Image2DMem(m_height + 1, m_width + 1);

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
		}
	}
	for (i = 0; i < m_height - 1; i += M) {
		for (j = 0; j < m_width - 1; j += M) {
			for (n = 0; n < M; n++) {
				for (m = 0; m < M; m++) {
					Mask[n * M + m] = m_tempImage[i + n][j + m];
				}
			}
			OnBubbleSort(Mask, M * M);
			Value = Mask[(int)(M * M / 2)];
			m_OutputImage[index] = (unsigned char)Value;
			index++;
		}
	}
}
```

- OnMeanSub : 평균 서브 샘플링

```cpp
void CImageProcessing2021108030Doc::OnMeanSub()
{
	int i, j, n, m, M = 4, index = 0, k; // M = 서브 샘플링 비율
	double* Mask, Value, Sum = 0.0;

	Mask = new double[M * M];

	m_Re_height = m_height / M;
	m_Re_width = m_width / M;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];
	m_tempImage = Image2DMem(m_height + 1, m_width + 1);

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
		}
	}
	for (i = 0; i < m_height - 1; i += M) {
		for (j = 0; j < m_width - 1; j += M) {
			for (n = 0; n < M; n++) {
				for (m = 0; m < M; m++) {
					Mask[n * M + m] = m_tempImage[i + n][j + m];
				}
			}
			for (k = 0; k < M * M; k++)
				Sum += Mask[k];
			Value = (Sum / (M * M));
			m_OutputImage[index] = (unsigned char)Value;
			index++;
			Sum = 0.0;
		}
	}
}
```

---

# 🧑‍💻 9장 - 이동, 대칭 ,회전

- OnTranslation : 영상 이동 함수

```cpp
void CImageProcessing2021108030Doc::OnTranslation()
{
	CImageTranslation dlg;

	if (dlg.DoModal() == IDOK) {
		int i, j;
		int h_pos = dlg.m_TranslationY, w_pos = dlg.m_TranslationX;
		double** tempArray;

		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;

		m_OutputImage = new unsigned char[m_Re_size];

		m_tempImage = Image2DMem(m_height, m_width);
		tempArray = Image2DMem(m_Re_height, m_Re_width);

		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
			}
		}

		for (i = 0; i < m_height - h_pos; i++) {
			for (j = 0; j < m_width - w_pos; j++) {
				tempArray[i + h_pos][j + w_pos] = m_tempImage[i][j];
			}
		}

		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				m_OutputImage[i * m_Re_width + j] = (unsigned char)tempArray[i][j];
			}
		}

		delete[] m_tempImage;
		delete[] tempArray;
	}
}
```

- OnMirrorHor : 영상 좌우 대칭 함수 → 💯영상 상하 대칭 함수도 작성할 수 있어야 함

```cpp
void CImageProcessing2021108030Doc::OnMirrorHor()
{
	int i, j;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	for (i = 0; i < m_height; i++) {
		for (j = 0; j < m_width; j++) {
			m_OutputImage[i * m_width + m_width - j - 1] = m_InputImage[i * m_width + j];
		}
	}
}
```

- OnRotation : 영상 회전 함수

```cpp
void CImageProcessing2021108030Doc::OnRotation()
{
	CImageRotation dlg;
	int i, j, CenterH, CenterW, newH, newW, degree;
	double Radian, PI, ** tempArray, Value;
	
	if (dlg.DoModal() == IDOK) {
		//최종회전각도 = 시계방향 각도 - 반시계방향 각도
		degree = dlg.m_Rotation - dlg.m_ReverseRotation;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];
		PI = 3.14159265358979;
		CenterH = m_height / 2;
		CenterW = m_width / 2;

		m_tempImage = Image2DMem(m_height, m_width);
		tempArray = Image2DMem(m_Re_height, m_Re_width);

		for (i = 0; i < m_height; i++) {
			for (j = 0; j < m_width; j++) {
				m_tempImage[i][j] = (double)m_InputImage[i * m_width + j];
			}
		}
		//최종회전각도가 양수여서 시계방향으로 회전할 경우
		if (degree >= 0) {
			Radian = (double)degree * PI / 180.0;
			for (i = 0; i < m_height; i++) {
				for (j = 0; j < m_width; j++) {
					newH = (int)((i - CenterH) * cos(Radian) - (j - CenterW) * sin(Radian) + CenterH);
					newW = (int)((i - CenterH) * sin(Radian) + (j - CenterW) * cos(Radian) + CenterW);

					if (newH < 0 || newH >= m_height) {
						Value = 0;
					}
					else if (newW < 0 || newW >= m_width) {
						Value = 0;
					}
					else {
						Value = m_tempImage[newH][newW];
					}
					tempArray[i][j] = Value;
				}
			}
		}
		//최종회전각도가 음수여서 반시계방향으로 회전할 경우
		else {
			degree = -degree;
			Radian = (double)degree * PI / 180.0;
			for (i = 0; i < m_height; i++) {
				for (j = 0; j < m_width; j++) {
					newH = (int)((i - CenterH) * cos(Radian) + (j - CenterW) * sin(Radian) + CenterH);
					newW = (int)((i - CenterH) * sin(Radian) - (j - CenterW) * cos(Radian) + CenterW);

					if (newH < 0 || newH >= m_height) {
						Value = 0;
					}
					else if (newW < 0 || newW >= m_width) {
						Value = 0;
					}
					else {
						Value = m_tempImage[newH][newW];
					}
					tempArray[i][j] = Value;
				}
			}
		}
		
		for (i = 0; i < m_Re_height; i++) {
			for (j = 0; j < m_Re_width; j++) {
				m_OutputImage[i * m_Re_width + j] = (unsigned char)tempArray[i][j];
			}
		}

		delete[] m_tempImage;
		delete[] tempArray;
	}
}
```

---

# 🧑‍💻 10장 - 프레임 처리

- OnFrameSum : 프레임 덧셈

```cpp
void CImageProcessing2021108030Doc::OnFrameSum()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	CImageFrameDlg dlg;
	int i;
	double alpha;
	if (dlg.DoModal() == IDOK) {
		alpha = dlg.m_Alpha;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		if (OpenDlg.DoModal() == IDOK) {
			File.Open(OpenDlg.GetFileName(), CFile::modeRead);
		}
		if (File.GetLength() == (unsigned)m_width * m_height) {
			m_MiddleImage = new unsigned char[m_size];
			File.Read(m_MiddleImage, m_size);
			File.Close();

			for (i = 0; i < m_size; i++) {
				if ((alpha * m_InputImage[i] + (1 - alpha) * m_MiddleImage[i]) > 255)
					m_OutputImage[i] = 255;
				else
					m_OutputImage[i] = (unsigned char)(alpha * m_InputImage[i] + (1 - alpha) * m_MiddleImage[i]);
			}
		}
		else {
			AfxMessageBox("Image size not matched");
			return;
		}
	}
}
```

- OnFrameSub : 프레임 뻴셈

```cpp
void CImageProcessing2021108030Doc::OnFrameSub()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	CImageFrameDlg dlg;
	int i;
	double alpha;
	if (dlg.DoModal() == IDOK) {
		alpha = dlg.m_Alpha;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		if (OpenDlg.DoModal() == IDOK) {
			File.Open(OpenDlg.GetFileName(), CFile::modeRead);
		}
		if (File.GetLength() == (unsigned)m_width * m_height) {
			m_MiddleImage = new unsigned char[m_size];
			File.Read(m_MiddleImage, m_size);
			File.Close();

			for (i = 0; i < m_size; i++) {
				if ((alpha * m_InputImage[i] - (1 - alpha) * m_MiddleImage[i]) < 0)
					m_OutputImage[i] = 0;
				else
					m_OutputImage[i] = (unsigned char)(alpha * m_InputImage[i] - (1 - alpha) * m_MiddleImage[i]);
			}
		}
		else {
			AfxMessageBox("Image size not matched");
			return;
		}
	}
}
```

- OnFrameMul : 프레임 곱셈

```cpp
void CImageProcessing2021108030Doc::OnFrameMul()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	CImageFrameDlg dlg;
	int i;
	double alpha;
	if (dlg.DoModal() == IDOK) {
		alpha = dlg.m_Alpha;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		if (OpenDlg.DoModal() == IDOK) {
			File.Open(OpenDlg.GetFileName(), CFile::modeRead);
		}
		if (File.GetLength() == (unsigned)m_width * m_height) {
			m_MiddleImage = new unsigned char[m_size];
			File.Read(m_MiddleImage, m_size);
			File.Close();

			for (i = 0; i < m_size; i++) {
				if ((alpha * m_InputImage[i]) * ((1 - alpha) * m_MiddleImage[i]) > 255)
					m_OutputImage[i] = 255;
				else
					m_OutputImage[i] = (unsigned char)((alpha * m_InputImage[i]) * ((1 - alpha) * m_MiddleImage[i]));
			}
		}
		else {
			AfxMessageBox("Image size not matched");
			return;
		}
	}
}
```

- OnFrameDiv : 프레임 나눗셈💯

```cpp
void CImageProcessing2021108030Doc::OnFrameDiv()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	CImageFrameDlg dlg;
	int i;
	double alpha;
	if (dlg.DoModal() == IDOK) {
		alpha = dlg.m_Alpha;
		m_Re_height = m_height;
		m_Re_width = m_width;
		m_Re_size = m_Re_height * m_Re_width;
		m_OutputImage = new unsigned char[m_Re_size];

		if (OpenDlg.DoModal() == IDOK) {
			File.Open(OpenDlg.GetFileName(), CFile::modeRead);
		}
		if (File.GetLength() == (unsigned)m_width * m_height) {
			m_MiddleImage = new unsigned char[m_size];
			File.Read(m_MiddleImage, m_size);
			File.Close();

			for (i = 0; i < m_size; i++) {
				if (m_InputImage[i] == 0)
					m_OutputImage[i] = 0;
				else if (m_MiddleImage[i] == 0)
					m_OutputImage[i] = 255;
				else
					m_OutputImage[i] = (unsigned char)((alpha*m_InputImage[i]) / ((1-alpha)* m_MiddleImage[i]));
			}
		}
		else {
			AfxMessageBox("Image size not matched");
			return;
		}
	}
}
```

- OnFrameAnd : 프레임AND연산

```cpp
void CImageProcessing2021108030Doc::OnFrameAnd()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	if (OpenDlg.DoModal() == IDOK) {
		File.Open(OpenDlg.GetFileName(), CFile::modeRead);
	}
	if (File.GetLength() == (unsigned)m_width * m_height) {
		m_MiddleImage = new unsigned char[m_size];
		File.Read(m_MiddleImage, m_size);
		File.Close();

		for (i = 0; i < m_size; i++) {
			m_OutputImage[i] = (unsigned char)(m_InputImage[i] & m_MiddleImage[i]);
		}
	}
	else {
		AfxMessageBox("Image size not matched");
		return;
	}
}
```

- OnFrameOr : 프레임OR연산

```cpp
void CImageProcessing2021108030Doc::OnFrameOr()
{
	CFile File;
	CFileDialog OpenDlg(TRUE);
	int i;
	m_Re_height = m_height;
	m_Re_width = m_width;
	m_Re_size = m_Re_height * m_Re_width;
	m_OutputImage = new unsigned char[m_Re_size];

	if (OpenDlg.DoModal() == IDOK) {
		File.Open(OpenDlg.GetFileName(), CFile::modeRead);
	}
	if (File.GetLength() == (unsigned)m_width * m_height) {
		m_MiddleImage = new unsigned char[m_size];
		File.Read(m_MiddleImage, m_size);
		File.Close();

		for (i = 0; i < m_size; i++) {
			m_OutputImage[i] = (unsigned char)(m_InputImage[i] | m_MiddleImage[i]);
		}
	}
	else {
		AfxMessageBox("Image size not matched");
		return;
	}
}
```