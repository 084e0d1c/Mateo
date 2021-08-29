
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'home', component: () => import('src/pages/HomePage.vue') },
      { path: 'loans', component: () => import('pages/LoansPage.vue'), children:[] },
      { path: 'loanDetails/:loanName', component: () => import('pages/LoanDetailsPage.vue') },
      { path: 'bankLoan', meta:{header:'Apply Bank Loan'}, component: () => import('src/pages/BankLoanPage.vue') },
      { path: 'loanPool', meta:{header:'Loan Pools'}, component: () => import('src/pages/LoanPoolPage.vue') },
      { path: 'loanPoolDetailsBorrow/:loanName',  component: () => import('src/pages/LoanPoolDetailsPageBorrow.vue') },
      { path: 'loanPoolDetailsContribute/:loanName',  component: () => import('src/pages/LoanPoolDetailsPageContribute.vue') },
      { path: 'loanContributionWithdrawal/:loanName',  component: () => import('src/pages/LoanContributionWithdrawalPage.vue') },
      { path: 'insurance', component: () => import('src/pages/InsurancePage.vue') },
      { path: 'learn', meta:{header:'Learn'}, component: () => import('src/pages/LearnPage.vue') },
      { path: 'profile', component: () => import('src/pages/ProfilePage.vue') },
      { path: 'bnpl', component: () => import('src/pages/bnplPage.vue') },
      
      { path: 'login', component: () => import('src/pages/LoginPage.vue') },
      
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
