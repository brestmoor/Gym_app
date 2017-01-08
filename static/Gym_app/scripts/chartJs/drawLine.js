Chart.types.Line.extend({
    name: "LineWithLine",
    initialize: function () {
        Chart.types.Line.prototype.initialize.apply(this, arguments);
    },
   draw: function () {
        Chart.types.Line.prototype.draw.apply(this, arguments);

        var lines = this.options.limitLines;

        for (var i = lines.length; --i >= 0;) {

            var xStart = Math.round(this.scale.xScalePaddingLeft);
            var linePositionY = this.scale.calculateY(lines[i].value);

            this.chart.ctx.fillStyle = lines[i].color ? lines[i].color : this.scale.textColor;
            this.chart.ctx.font = this.scale.font;
            this.chart.ctx.textAlign = "left";
            this.chart.ctx.textBaseline = "top";

            if (this.scale.showLabels && lines[i].label) {
                this.chart.ctx.fillText(lines[i].label, xStart + 5, linePositionY);
            }

            this.chart.ctx.lineWidth = this.scale.gridLineWidth;
            this.chart.ctx.strokeStyle = lines[i].color ? lines[i].color : this.scale.gridLineColor;

            if (this.scale.showHorizontalLines) {
                this.chart.ctx.beginPath();
                this.chart.ctx.moveTo(xStart, linePositionY);
                this.chart.ctx.lineTo(this.scale.width, linePositionY);
                this.chart.ctx.stroke();
                this.chart.ctx.closePath();
            }

            this.chart.ctx.lineWidth = this.lineWidth;
            this.chart.ctx.strokeStyle = this.lineColor;
            this.chart.ctx.beginPath();
            this.chart.ctx.moveTo(xStart - 5, linePositionY);
            this.chart.ctx.lineTo(xStart, linePositionY);
            this.chart.ctx.stroke();
            this.chart.ctx.closePath();
        }
    }
});