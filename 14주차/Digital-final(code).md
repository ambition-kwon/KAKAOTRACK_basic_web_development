# Digital-final(Code)

# π§βπ»Β 6μ₯ - νμμμ­μ²λ¦¬

- Image2DMem : νμ μμ­ μ²λ¦¬ νλ‘κ·Έλ¨μ κ°λ¨ν νλ €κ³  **1μ°¨μ λ°°μ΄μ 2μ°¨μ λ°°μ΄λ‘ ν λΉ**νλ ν¨μ

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

- OnMaskProcess : νμ μμ­μ μ²λ¦¬νλ ν¨μ

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

- OnEmbossing : μ λ³΄μ± ν¨μ

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
	//μν : &λ₯Ό λΆμ¬ μλλκ² λ°κΏλ³΄μλΌ!
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

- OnBlurr : λΈλ¬λ§ ν¨μ

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

- OnGaussianFilter : μ€λ¬΄λ© μ²λ¦¬ μ€ κ°μ°μμ νν° μ¬μ© ν¨μ

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

- OnSharpening : μ€νλ ν¨μ

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

- OnHpfSharp : κ³ μ£Όν νν° μ€νλ ν¨μ

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

# π§βπ»Β 7μ₯ - μμ§ κ²μΆ

- OnDiffOperator : μ΄λκ³Ό μ°¨λΆ(1 : μν, 2 : μμ§)

```cpp
void CImageProcessing2021108030Doc::OnDiffOperator()
{
	int i, j;
	double DiffHorMask1[3][3] = { {0., -1., 0.},{0., 1., 0.},{0., 0., 0.} }; //μν
	double DiffHorMask2[3][3] = { {0., 0., 0.},{-1., 1., 0.},{0., 0., 0.} }; //μμ§
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

- DoubleABS : μ λκ° λ³ν ν¨μ

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

- OnHomogenOperator : μ μ¬ μ°μ°μ κΈ°λ²

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

- OnHomogenOperatorThreshold : μ μ¬ μ°μ°μ κΈ°λ² + μκ³κ° μΆκ°

```cpp
void CImageProcessing2021108030Doc::OnHomogenOperatorThreshold()
{
	int i, j, n, m;
	double max, ** tempOutputImage;
	CHomogenOperatorThresholdDlg dlg;
	if (dlg.DoModal() == IDOK) { //dialogμμ OKκ° λλ Έμ κ²½μ° μ€ν
		//SWAP(μλ ₯λ°λ 2κ°μ λ³μ μ€ λ¬΄μμ΄ λ κ°μ΄ ν΄μ§ λͺ¨λ₯΄κΈ° λλ¬Έμ val1 <= val2λ₯Ό μ μ§νκΈ° μν μ½λ)
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
				//λ€μ€ μκ³κ°μΌλ‘ μ²λ¦¬νκΈ° μν μ½λ(λ¨, val1 <= val2)
				//λ κ²½κ³ κ° λ³΄λ€ ν° κ°μ΄ μ¬ κ²½μ° 255λ‘ μ΄κΈ°ν 
				//λ κ²½κ³ κ° μ¬μ΄μ κ°μ΄ μ¬ κ²½μ° κ°μ₯ ν° κ²½κ³κ°μΌλ‘ μ΄κΈ°ν
				//λ κ²½κ³ κ° λ³΄λ€ μμ κ°μ΄ μ¬ κ²½μ° 0μΌλ‘ μ΄κΈ°ν
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

# π§βπ»Β 8μ₯ - κΈ°ννμ  λ³ν

- OnNearest : κ°μ₯ μΈμ ν μ΄μνμ λ³΄κ°λ²

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

- OnBilinear : μμ ν λ³΄κ°λ²

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

- OnMedianSub : λ―ΈλμΈ μλΈ μνλ§

```cpp
void CImageProcessing2021108030Doc::OnMedianSub()
{
	int i, j, n, m, M = 4, index = 0; // M = μλΈ μνλ§ λΉμ¨
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

- OnMeanSub : νκ·  μλΈ μνλ§

```cpp
void CImageProcessing2021108030Doc::OnMeanSub()
{
	int i, j, n, m, M = 4, index = 0, k; // M = μλΈ μνλ§ λΉμ¨
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

# π§βπ»Β 9μ₯ - μ΄λ, λμΉ­ ,νμ 

- OnTranslation : μμ μ΄λ ν¨μ

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

- OnMirrorHor : μμ μ’μ° λμΉ­ ν¨μ β π―μμ μν λμΉ­ ν¨μλ μμ±ν  μ μμ΄μΌ ν¨

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

- OnRotation : μμ νμ  ν¨μ

```cpp
void CImageProcessing2021108030Doc::OnRotation()
{
	CImageRotation dlg;
	int i, j, CenterH, CenterW, newH, newW, degree;
	double Radian, PI, ** tempArray, Value;
	
	if (dlg.DoModal() == IDOK) {
		//μ΅μ’νμ κ°λ = μκ³λ°©ν₯ κ°λ - λ°μκ³λ°©ν₯ κ°λ
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
		//μ΅μ’νμ κ°λκ° μμμ¬μ μκ³λ°©ν₯μΌλ‘ νμ ν  κ²½μ°
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
		//μ΅μ’νμ κ°λκ° μμμ¬μ λ°μκ³λ°©ν₯μΌλ‘ νμ ν  κ²½μ°
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

# π§βπ»Β 10μ₯ - νλ μ μ²λ¦¬

- OnFrameSum : νλ μ λ§μ

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

- OnFrameSub : νλ μ λ»΄μ

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

- OnFrameMul : νλ μ κ³±μ

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

- OnFrameDiv : νλ μ λλμπ―

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

- OnFrameAnd : νλ μANDμ°μ°

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

- OnFrameOr : νλ μORμ°μ°

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