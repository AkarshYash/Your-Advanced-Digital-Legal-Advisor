# 🚀 Quick Deployment Guide - LegalEase AI Advanced

## Step-by-Step FREE Deployment (5 Minutes)

### 📋 Prerequisites
- GitHub account
- Gemini API key (free from Google AI Studio)

---

## 🎯 Method 1: Deploy on Render.com (Easiest)

### Step 1: Prepare Your Project (2 minutes)

1. **Run the deployment preparation script:**
```bash
python deploy.py
```

2. **Edit the `.env` file with your API key:**
```env
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here-change-this
GEMINI_API_KEY=your-actual-gemini-api-key-here
```

3. **Get your Gemini API key (FREE):**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with Google account
   - Click "Create API Key"
   - Copy the key and paste in `.env` file

### Step 2: Push to GitHub (1 minute)

1. **Create a new repository on GitHub:**
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name it: `legalease-ai-advanced`
   - Make it public
   - Don't initialize with README (we already have files)

2. **Push your code:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/legalease-ai-advanced.git
git push -u origin main
```

### Step 3: Deploy on Render.com (2 minutes)

1. **Go to [render.com](https://render.com)**
2. **Sign up with GitHub**
3. **Click "New +" → "Web Service"**
4. **Connect your `legalease-ai-advanced` repository**
5. **Configure settings:**
   - **Name:** `legalease-ai-advanced`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements-deploy.txt`
   - **Start Command:** `gunicorn run:app`
   - **Instance Type:** `Free`

6. **Add Environment Variables:**
   - Click "Environment" tab
   - Add: `FLASK_ENV` = `production`
   - Add: `SECRET_KEY` = `your-secret-key`
   - Add: `GEMINI_API_KEY` = `your-gemini-api-key`

7. **Click "Create Web Service"**

### Step 4: Access Your Live App! 🎉

Your app will be live at: `https://legalease-ai-advanced.onrender.com`

---

## 🎯 Method 2: Deploy on Railway.app (Alternative)

### Quick Railway Deployment:

1. **Go to [railway.app](https://railway.app)**
2. **Sign up with GitHub**
3. **Click "New Project" → "Deploy from GitHub repo"**
4. **Select your repository**
5. **Add Environment Variables:**
   - `FLASK_ENV` = `production`
   - `SECRET_KEY` = `your-secret-key`
   - `GEMINI_API_KEY` = `your-gemini-api-key`
   - `PORT` = `5000`
6. **Deploy automatically starts**

Your app will be live at: `https://legalease-ai-advanced.up.railway.app`

---

## 🎯 Method 3: Deploy on Vercel (Serverless)

### Quick Vercel Deployment:

1. **Install Vercel CLI:**
```bash
npm i -g vercel
```

2. **Login and deploy:**
```bash
vercel login
vercel --prod
```

3. **Follow the prompts and add environment variables**

---

## 🔧 Troubleshooting

### Common Issues:

1. **Build fails:**
   - Check `requirements-deploy.txt` has correct package versions
   - Ensure Python version matches `runtime.txt`

2. **App crashes:**
   - Check environment variables are set correctly
   - Verify Gemini API key is valid

3. **Database errors:**
   - App uses SQLite by default (no setup needed)
   - Database file is created automatically

### Getting Help:

- **Email:** chatuvrdiakarsh51@gmail.com
- **WhatsApp:** +91 7742148084
- **GitHub Issues:** Create an issue in your repository

---

## 🌟 Success! Your LegalEase AI is Live!

### What's Next:

1. **Test all features** on your live app
2. **Share the link** with friends and colleagues
3. **Monitor usage** through platform dashboards
4. **Add custom domain** (optional)
5. **Set up monitoring** with UptimeRobot (free)

### Your Live Features:
- ✅ AI-Powered Legal Assistant
- ✅ Document Analysis & Generation
- ✅ Expert Lawyer Network
- ✅ Legal Resources Library
- ✅ Multi-language Support
- ✅ Real-time Chat Interface
- ✅ Student Tools & Games
- ✅ Case Study Analyzer

---

## 📊 Free Tier Limits:

### Render.com:
- 750 hours/month (enough for 24/7)
- 512MB RAM
- Sleeps after 15min inactivity

### Railway.app:
- $5 credit monthly
- Pay-as-you-go after credit

### Vercel:
- 100GB bandwidth/month
- Serverless functions

---

## 🎉 Congratulations!

Your **LegalEase AI Advanced** is now live and helping people access legal knowledge worldwide!

**Live URL Examples:**
- Render: `https://legalease-ai-advanced.onrender.com`
- Railway: `https://legalease-ai-advanced.up.railway.app`
- Vercel: `https://legalease-ai-advanced.vercel.app`

---

*🚀 Built with ❤️ by Akarsh Chaturvedi*
*📧 Contact: chatuvrdiakarsh51@gmail.com*