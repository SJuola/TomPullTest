/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QTabWidget *tabWidget;
    QWidget *Tab1;
    QHBoxLayout *horizontalLayout_2;
    QHBoxLayout *horizontalLayout;
    QGraphicsView *graphicsView;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *pushButton_3;
    QVBoxLayout *verticalLayout_2;
    QSpacerItem *verticalSpacer_2;
    QLabel *label_2;
    QLabel *label;
    QSpacerItem *verticalSpacer;
    QPushButton *pushButton_4;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QWidget *tab_2;
    QVBoxLayout *verticalLayout_4;
    QVBoxLayout *verticalLayout_3;
    QSlider *horizontalSlider;
    QLabel *label_3;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 480);
        MainWindow->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"}\n"
"\n"
"graphicsView\n"
"{\n"
"	background: rgb(180,180,180);\n"
"}\n"
""));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setEnabled(true);
#ifndef QT_NO_WHATSTHIS
        centralWidget->setWhatsThis(QString::fromUtf8(""));
#endif // QT_NO_WHATSTHIS
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setTabPosition(QTabWidget::East);
        tabWidget->setTabShape(QTabWidget::Rounded);
        Tab1 = new QWidget();
        Tab1->setObjectName(QString::fromUtf8("Tab1"));
        horizontalLayout_2 = new QHBoxLayout(Tab1);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        graphicsView = new QGraphicsView(Tab1);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setMinimumSize(QSize(320, 0));
        graphicsView->setStyleSheet(QString::fromUtf8("width: 60%"));

        horizontalLayout->addWidget(graphicsView);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(20, -1, -1, -1);
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        pushButton_3 = new QPushButton(Tab1);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setMinimumSize(QSize(0, 100));
        QFont font;
        font.setFamily(QString::fromUtf8("Monospace"));
        font.setPointSize(30);
        font.setBold(true);
        font.setWeight(75);
        pushButton_3->setFont(font);

        horizontalLayout_3->addWidget(pushButton_3);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, -1, -1);
        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Minimum);

        verticalLayout_2->addItem(verticalSpacer_2);

        label_2 = new QLabel(Tab1);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy);
        QFont font1;
        font1.setFamily(QString::fromUtf8("Monospace"));
        font1.setPointSize(30);
        label_2->setFont(font1);
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(label_2);

        label = new QLabel(Tab1);
        label->setObjectName(QString::fromUtf8("label"));
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(0, 25));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Monospace"));
        label->setFont(font2);
        label->setAutoFillBackground(true);
        label->setStyleSheet(QString::fromUtf8(""));
        label->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(label);

        verticalSpacer = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Minimum);

        verticalLayout_2->addItem(verticalSpacer);


        horizontalLayout_3->addLayout(verticalLayout_2);

        pushButton_4 = new QPushButton(Tab1);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        pushButton_4->setMinimumSize(QSize(0, 100));
        pushButton_4->setFont(font);

        horizontalLayout_3->addWidget(pushButton_4);


        verticalLayout->addLayout(horizontalLayout_3);

        pushButton_2 = new QPushButton(Tab1);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setMinimumSize(QSize(0, 75));
        QFont font3;
        font3.setFamily(QString::fromUtf8("FreeSans"));
        font3.setPointSize(18);
        font3.setBold(true);
        font3.setWeight(75);
        pushButton_2->setFont(font3);

        verticalLayout->addWidget(pushButton_2);

        pushButton = new QPushButton(Tab1);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setMinimumSize(QSize(0, 75));
        pushButton->setFont(font3);

        verticalLayout->addWidget(pushButton);


        horizontalLayout->addLayout(verticalLayout);


        horizontalLayout_2->addLayout(horizontalLayout);

        tabWidget->addTab(Tab1, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        verticalLayout_4 = new QVBoxLayout(tab_2);
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setContentsMargins(11, 11, 11, 11);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(20);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(10, 30, 10, 30);
        horizontalSlider = new QSlider(tab_2);
        horizontalSlider->setObjectName(QString::fromUtf8("horizontalSlider"));
        QFont font4;
        font4.setPointSize(30);
        horizontalSlider->setFont(font4);
        horizontalSlider->setMaximum(100);
        horizontalSlider->setSingleStep(1);
        horizontalSlider->setSliderPosition(20);
        horizontalSlider->setOrientation(Qt::Horizontal);
        horizontalSlider->setTickPosition(QSlider::TicksBelow);

        verticalLayout_3->addWidget(horizontalSlider);

        label_3 = new QLabel(tab_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setFont(font4);
        label_3->setAlignment(Qt::AlignCenter);

        verticalLayout_3->addWidget(label_3);


        verticalLayout_4->addLayout(verticalLayout_3);

        tabWidget->addTab(tab_2, QString());

        gridLayout->addWidget(tabWidget, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Tom Accelerated Pull Test", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "-", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "50", nullptr));
        label->setText(QApplication::translate("MainWindow", "In/s", nullptr));
        pushButton_4->setText(QApplication::translate("MainWindow", "+", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "Start", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "Log Data", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Tab1), QApplication::translate("MainWindow", "Test Mode", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "Current Position: 10/100", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("MainWindow", "Manual Control", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
