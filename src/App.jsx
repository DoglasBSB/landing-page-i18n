import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Star, Users, Globe, ArrowRight, CheckCircle } from 'lucide-react'
import './App.css'

function App() {
  const { t, i18n } = useTranslation()

  const toggleLanguage = () => {
    const newLang = i18n.language === 'pt' ? 'en' : 'pt'
    i18n.changeLanguage(newLang)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="container mx-auto px-4 py-6">
        <nav className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Globe className="h-8 w-8 text-blue-600" />
            <span className="text-2xl font-bold text-gray-900">TechSolutions</span>
          </div>
          <div className="flex items-center space-x-4">
            <Button variant="ghost">{t('nav.about')}</Button>
            <Button variant="ghost">{t('nav.services')}</Button>
            <Button variant="ghost">{t('nav.contact')}</Button>
            <Button 
              variant="outline" 
              onClick={toggleLanguage}
            >
              {i18n.language === 'pt' ? 'EN' : 'PT'}
            </Button>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-16 text-center">
        <Badge className="mb-4" variant="secondary">
          {t('hero.badge')}
        </Badge>
        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          {t('hero.title')}
          <span className="text-blue-600">{t('hero.title_highlight')}</span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
          {t('hero.description')}
        </p>
        <div className="flex justify-center space-x-4">
          <Button size="lg" className="px-8">
            {t('hero.cta.primary')}
            <ArrowRight className="ml-2 h-4 w-4" />
          </Button>
          <Button variant="outline" size="lg">
            {t('hero.cta.secondary')}
          </Button>
        </div>
      </section>

      {/* Stats Section */}
      <section className="container mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-600 mb-2">500+</div>
            <div className="text-gray-600">{t('stats.projects')}</div>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-600 mb-2">98%</div>
            <div className="text-gray-600">{t('stats.satisfaction')}</div>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-600 mb-2">24/7</div>
            <div className="text-gray-600">{t('stats.support')}</div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          {t('services.title')}
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                {t('services.web.title')}
              </CardTitle>
              <CardDescription>
                {t('services.web.description')}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                {t('services.web.content')}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Users className="h-5 w-5 text-blue-500 mr-2" />
                {t('services.consulting.title')}
              </CardTitle>
              <CardDescription>
                {t('services.consulting.description')}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                {t('services.consulting.content')}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Star className="h-5 w-5 text-yellow-500 mr-2" />
                {t('services.automation.title')}
              </CardTitle>
              <CardDescription>
                {t('services.automation.description')}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                {t('services.automation.content')}
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">
            {t('cta.title')}
          </h2>
          <p className="text-xl mb-8 opacity-90">
            {t('cta.description')}
          </p>
          <Button size="lg" variant="secondary" className="px-8">
            {t('cta.button')}
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <Globe className="h-6 w-6" />
                <span className="text-xl font-bold">TechSolutions</span>
              </div>
              <p className="text-gray-400">
                {t('footer.description')}
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t('footer.services.title')}</h3>
              <ul className="space-y-2 text-gray-400">
                <li>{t('footer.services.web')}</li>
                <li>{t('footer.services.mobile')}</li>
                <li>{t('footer.services.consulting')}</li>
                <li>{t('footer.services.automation')}</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t('footer.company.title')}</h3>
              <ul className="space-y-2 text-gray-400">
                <li>{t('footer.company.about')}</li>
                <li>{t('footer.company.team')}</li>
                <li>{t('footer.company.careers')}</li>
                <li>{t('footer.company.blog')}</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t('footer.contact.title')}</h3>
              <ul className="space-y-2 text-gray-400">
                <li>contato@techsolutions.com</li>
                <li>(11) 9999-9999</li>
                <li>São Paulo, SP</li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
            <p>{t('footer.copyright')}</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App

