namespace AlgorithmInCs.Figures
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnDrawEllipse = new System.Windows.Forms.Button();
            this.btnDrawArc = new System.Windows.Forms.Button();
            this.btnDrawLines = new System.Windows.Forms.Button();
            this.btnDrawPath = new System.Windows.Forms.Button();
            this.btnDrawRuler = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnDrawEllipse
            // 
            this.btnDrawEllipse.Location = new System.Drawing.Point(12, 308);
            this.btnDrawEllipse.Name = "btnDrawEllipse";
            this.btnDrawEllipse.Size = new System.Drawing.Size(75, 23);
            this.btnDrawEllipse.TabIndex = 0;
            this.btnDrawEllipse.Text = "Draw Ellipse";
            this.btnDrawEllipse.UseVisualStyleBackColor = true;
            this.btnDrawEllipse.Click += new System.EventHandler(this.btnDrawEllipse_Click);
            // 
            // btnDrawArc
            // 
            this.btnDrawArc.Location = new System.Drawing.Point(93, 308);
            this.btnDrawArc.Name = "btnDrawArc";
            this.btnDrawArc.Size = new System.Drawing.Size(75, 23);
            this.btnDrawArc.TabIndex = 1;
            this.btnDrawArc.Text = "Draw Arc";
            this.btnDrawArc.UseVisualStyleBackColor = true;
            this.btnDrawArc.Click += new System.EventHandler(this.btnDrawArc_Click);
            // 
            // btnDrawLines
            // 
            this.btnDrawLines.Location = new System.Drawing.Point(174, 308);
            this.btnDrawLines.Name = "btnDrawLines";
            this.btnDrawLines.Size = new System.Drawing.Size(75, 23);
            this.btnDrawLines.TabIndex = 2;
            this.btnDrawLines.Text = "Draw Lines";
            this.btnDrawLines.UseVisualStyleBackColor = true;
            this.btnDrawLines.Click += new System.EventHandler(this.btnDrawLines_Click);
            // 
            // btnDrawPath
            // 
            this.btnDrawPath.Location = new System.Drawing.Point(255, 308);
            this.btnDrawPath.Name = "btnDrawPath";
            this.btnDrawPath.Size = new System.Drawing.Size(75, 23);
            this.btnDrawPath.TabIndex = 3;
            this.btnDrawPath.Text = "Draw Path";
            this.btnDrawPath.UseVisualStyleBackColor = true;
            this.btnDrawPath.Click += new System.EventHandler(this.btnDrawPath_Click);
            // 
            // btnDrawRuler
            // 
            this.btnDrawRuler.Location = new System.Drawing.Point(336, 308);
            this.btnDrawRuler.Name = "btnDrawRuler";
            this.btnDrawRuler.Size = new System.Drawing.Size(75, 23);
            this.btnDrawRuler.TabIndex = 4;
            this.btnDrawRuler.Text = "Draw Ruler";
            this.btnDrawRuler.UseVisualStyleBackColor = true;
            this.btnDrawRuler.Click += new System.EventHandler(this.btnDrawRuler_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(446, 343);
            this.Controls.Add(this.btnDrawRuler);
            this.Controls.Add(this.btnDrawPath);
            this.Controls.Add(this.btnDrawLines);
            this.Controls.Add(this.btnDrawArc);
            this.Controls.Add(this.btnDrawEllipse);
            this.Name = "MainForm";
            this.Text = "Algorithm Figures";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.MainForm_Paint);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnDrawEllipse;
        private System.Windows.Forms.Button btnDrawArc;
        private System.Windows.Forms.Button btnDrawLines;
        private System.Windows.Forms.Button btnDrawPath;
        private System.Windows.Forms.Button btnDrawRuler;
    }
}

